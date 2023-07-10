from flask_restx import Namespace, Resource
from flask import request, jsonify
from app.models.models import Device
from app.utils.created_report import created_report, created_report_perfomance

from app.utils.logger import Logger

logger = Logger(__name__)

report_ns = Namespace('report', description="report")


@report_ns.route('/configuration')
class Report(Resource):
    @report_ns.doc(params={'serial':'specifie your serial'})
    def get(self):
        
        serial = request.args.get('serial', type=str)
        logger.logger.info(f"Initialzing request for report with the serial {serial}")

        if not serial:
            return jsonify({"response":"Unable to allocate the device"})
        
        data = Device.query.filter_by(serial=serial).first()

        data_formated = {
                'client_count':data.client_count,
                'firmware_version':data.firmware_version,
                'labels':data.labels, 
                'macaddr':data.macaddr,
                'model':data.model,
                'name':data.name,
                'serial':data.serial,
                'stack_id':data.stack_id, 
                'uplink_ports':data.uplink_ports
                }
        
        created_report(data_formated)
        logger.logger.info(f"Report was created for {data_formated}")

        return jsonify({"response":"Report was successfully created"})
    

@report_ns.route('/performace')
class PerformaceReport(Resource):
    @report_ns.doc(params={'serial':'specifie your serial'})
    def get(self):
        """Get performace report"""
        serial = request.args.get('serial', type=str)
        logger.logger.info(f"Initialzing request for performace with the serial {serial}")

        if not serial:
            return jsonify({"response":"Unable to allocate the device"})
        
        data = Device.query.filter_by(serial=serial).first()

        data_formated = {
                'cpu_utilization': data.cpu_utiization,
                'mem_free':data.mem_free,
                'mem_total':data.mem_total, 
                'name':data.name,
                'serial':data.serial,
                'status':data.status,
                'temperature':data.temperature,
                'uptime':data.uptime
                }
        
        created_report_perfomance(data_formated)
        logger.logger.info(f"Report Perfomace was created for {data_formated}")
        return jsonify({"response":"Performance report created"})