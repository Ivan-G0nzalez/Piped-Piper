from flask_restx import Namespace, Resource, fields
from flask import request, jsonify
from app.models.models import Device

from app.models.exts import db

from app.utils.logger import Logger

logger = Logger(__name__)

threshold_ns = Namespace('setting', description="setting")

threshold_model = threshold_ns.model(
    "threshold",
    {
        "threshold":fields.Integer()
    }
)



@threshold_ns.route('/memory')
class MemoryResource(Resource):
    @threshold_ns.doc(params={'serial':'specifie your serial'})
    def get(self):
        serial = request.args.get('serial', type=str)
        logger.logger.info(f"Initializing request to get Threshold for device with serial {serial}")
        
        if not serial:
            logger.logger.info(f"serial is required")
            return jsonify(message="serial is required")
            
        data = Device.query.filter_by(serial=serial).first()


        if not data:
            logger.logger.info(f"Unable to get the data")
            return jsonify({"response":"Unable to get data"})

        data_formated = {
            "mem_free":data.mem_free,
            "mem_total":data.mem_total,
            "threshold": data.threshold,
            "name":data.name,
            "serial":data.serial
        }

        if not data_formated['threshold']:
            logger.logger.info(f"No Threshold has been set up")
            return jsonify({"response":"No Threshold has been set up"})
        
        mem_free, mem_total, threshold = (data_formated["mem_free"], data_formated["mem_total"], data_formated["threshold"])

        used_mem = mem_total - mem_free
        memory_utilization = (used_mem / mem_total) * 100
    
        if  memory_utilization > threshold:
            logger.logger.info(f'The memory of the {data_formated.get("name")} with serial {data_formated.get("serial")} has exceeded the current threshold >= {data_formated.get("threshold")}%. The current value is {memory_utilization} %')
            return jsonify({'response': f'The memory of the {data_formated.get("name")} with serial {data_formated.get("serial")} has exceeded the current threshold >= {data_formated.get("threshold")}%. The current value is {memory_utilization} %'})

        return jsonify({"response":"The memory has not except the threshold"})
    
    @threshold_ns.expect(threshold_model)
    @threshold_ns.doc(params={'serial':'specifie your serial'})
    def put(self):
        logger.logger.info(f"setting a new threshold")
        serial = request.args.get('serial', type=str)
        if not serial:
            return jsonify(message="serial is required")

        limit = request.json["threshold"]

        if limit > 100 or limit < 0:
            return jsonify({"response":"Unable to set up the threshold, limit should be between 0-100"})
        
        Device.query.filter_by(serial=serial).update({"threshold": limit})

        db.session.commit()
        logger.logger.info(f"Threshold succefully updated")
        return jsonify({"response":"succefully updated"})
    

@threshold_ns.route("/cpu_utilization")
class CPUResouse(Resource):
    @threshold_ns.doc(params={'serial':'specifie your serial'})
    def get(self):
        serial = request.args.get('serial', type=str)
        logger.logger.info(f"Initializing request to get Threshold for device with serial {serial}")
        

        if not serial:
            jsonify(message="serial is required")

        data = Device.query.filter_by(serial=serial).first()

        if not data:
            return jsonify(message="Information not got it")

        data_formated = {
            "cpu_utilization": data.cpu_utiization,
            "threshold": data.threshold,
            "name": data.name,
            "serial": data.serial
        }

        if not data_formated["threshold"]:
            return jsonify(message="No Threshold has been set up")

        if data_formated["cpu_utilization"] > data_formated["threshold"]:
            logger.logger.info(f"The cpu_utilization of the {data.get('name')} with the serial {data.get('serial')} has exeeded the current threshold >= {data.get('threshold')}%. The current value is {data['cpu_utilization']}")
            return jsonify(message=f"The cpu_utilization of the {data.get('name')} with the serial {data.get('serial')} has exeeded the current threshold >= {data.get('threshold')}%. The current value is {data['cpu_utilization']}")


        logger.logger.info(f"The cpu has not exceded the threshold")

        return jsonify(message="The cpu has not exceded the threshold")