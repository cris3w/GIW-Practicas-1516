from bottle import get, run, template
from bson.code import Code
from bson.son import SON
from pymongo import MongoClient


# MapReduce: usuarios en cada pais.
@get('/users_by_country_mr')
def users_by_country_mr():
    
    client = MongoClient('localhost', 27017)
    
    mapper = Code("""
                function map() {
                    emit(this.country, {count: 1});
                }
                """)
    
    reducer = Code("""
                function reduce(key, values) {
                    var result = 0;
                    for (var i = 0; i < values.length; i++) {
                        result = result + values[i].count;
                    }
                    return {count: NumberInt(result)}
                }
                """)
    
    results = client['giw'].users.inline_map_reduce(mapper, reducer)
    
    return template('vistas/users-by-country-mr.tpl', results=results)
    

# Aggregation Pipeline: usuarios en cada pais (orden descendente por numero de usuarios).
@get('/users_by_country_agg')
def users_by_country_agg():
    
    client = MongoClient('localhost', 27017)
    
    pipeline = [
        {"$group": {"_id": "$country", "count": {"$sum": 1}}},
        {"$sort": SON([("count", -1)])}
    ]
    
    results = list(client['giw'].users.aggregate(pipeline));
    
    return template('vistas/users-by-country-agg.tpl', results=results)
    
    
# MapReduce: gasto total en cada pais.
@get('/spending_by_country_mr')
def spending_by_country_mr():
    
    client = MongoClient('localhost', 27017)

    mapper = Code("""
                function map() {
                    var suma = 0;
                    if (this.orders) {
                        for (var i = 0; i < this.orders.length; i++) {
                            suma = suma + this.orders[i].total;
                        }
                    }
                    emit(this.country, {count: suma});
                }
                """)
    
    reducer = Code("""
                function reduce(key, values) {
                    var result = 0;
                    for (var i = 0; i < values.length; i++) {
                        result = result + values[i].count;
                    }
                    return {count: result}
                }
                """)
    
    results = client['giw'].users.inline_map_reduce(mapper, reducer)
   
    return template('vistas/spending-by-country-mr.tpl', results=results)


# Aggregation Pipeline: gasto total en cada pais (orden descendente por nombre del pais).
@get('/spending_by_country_agg')
def spending_by_country_agg():
    
    client = MongoClient('localhost', 27017)
    
    pipeline = [
        {"$unwind": "$orders"},
        {"$group": {"_id": "$country", "count": {"$sum": "$orders.total"}}},
        {"$sort": SON([("_id", 1)])}
    ]
    
    results = list(client['giw'].users.aggregate(pipeline));
    
    return template('vistas/spending-by-country-agg.tpl', results=results)


# MapReduce: gasto total realizado por las mujeres que han realizado EXACTAMENTE 3 compras.
@get('/spending_female_3_orders_mr')
def spending_female_3_orders_mr():
    
    client = MongoClient('localhost', 27017)

    mapper = Code("""
                function map() {
                    var suma = 0;
                    if (this.gender == "Female") {
                        if (this.orders) {
                            if (this.orders.length == 3) {
                                for (var i = 0; i < this.orders.length; i++) {
                                    suma = suma + this.orders[i].total;
                                }
                            }
                        }
                    }
                    emit(this.country, {count: suma});
                }
                """)
    
    reducer = Code("""
                function reduce(key, values) {
                    var result = 0;
                    for (var i = 0; i < values.length; i++) {
                        result = result + values[i].count;
                    }
                    return {count: result}
                }
                """)
    
    results = client['giw'].users.inline_map_reduce(mapper, reducer)
    
    total = 0
    if len(results) > 0:
        i = 0
        while (i < len(results)):
            total = total + results[i]['value']['count']
            i = i + 1
    
    return template('vistas/spending-female-3-orders-mr.tpl', total=total)


# Aggregation Pipeline: gasto total realizado por las mujeres que han realizado EXACTAMENTE 3 compras.
@get('/spending_female_3_orders_agg')
def spending_female_3_orders_agg():
    
    client = MongoClient('localhost', 27017)
    
    pipeline = [
        {"$match": { "gender": "Female", "orders": {"$size": 3}}},
        {"$unwind": "$orders"},
        {"$group": {"_id": "$country", "count": {"$sum": "$orders.total"}}},
    ]
    
    results = list(client['giw'].users.aggregate(pipeline))
    
    total = 0
    if len(results) > 0:
        i = 0
        while (i < len(results)):
            total = total + results[i]['count']
            i = i + 1
    
    return template('vistas/spending-female-3-orders-agg.tpl', total=total)


if __name__ == "__main__":
    run(host='localhost', port=80, debug=True)
