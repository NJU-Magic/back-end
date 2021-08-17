from DAO.dao_utils import *

def addAlgorithmResData(sensor_data_id, algorithm_type, algorithm_name, algorithm_result):
    '''
    params:
    sensor_data_id   type:int
    algorithm_type   type:int
    algorithm_name   type:str
    algorithm_result type:str
    '''
    database = Database(DATABASE_PATH)

    database.update("insert into AlgorithmRes (sensor_data_id, \
                                              algorithm_type,\
                                              algorithm_name, \
                                              algorithm_result) values\
                                              ({}, {}, '{}', '{}')".format(
        sensor_data_id,
        algorithm_type,
        algorithm_name,
        algorithm_result,))

def queryAlgorithmBySensorId(SensorID):
    '''
    params:
    SensorID   type:int
    '''
    database = Database(DATABASE_PATH)

    cursor = database.query("select * from AlgorithmRes where sensor_data_id={}".format(SensorID))

    data = []
    for row in cursor:
        data.append({
            "algorithm_res_id" : row[0],
            "sensor_data_id": row[1],
            "algorithm_type": row[2],
            "algorithm_name": row[3],
            "algorithm_result": row[4],
        })

    return data