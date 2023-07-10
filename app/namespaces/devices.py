from flask_restx import Namespace, Resource, fields, abort
from flask import request, jsonify
from app.models.models import Device
from werkzeug.exceptions import InternalServerError, NotFound

from app.utils.logger import Logger

logger = Logger(__name__)

import uuid


devices_ns = Namespace('devices', description="Devices")


device_model = devices_ns.model(
    "Device",
    {
        "id": fields.Integer(), 
        "client_count": fields.Integer(),
        "cpu_utiization":fields.Float(),
        "firmware_version":fields.String(),
        "labels": fields.String(),
        "macaddr":fields.String(),
        "mem_free": fields.Integer(),
        "mem_total": fields.Integer(),
        "model": fields.String(),
        "name": fields.String(),
        "serial": fields.String(),
        "stack_id": fields.Integer(),
        "status": fields.String(),
        "temperature":fields.String(),
        "uptime":fields.Integer(),
        "uplink_ports": fields.String(),
        "components_id": fields.Integer()
    }
)


@devices_ns.route('/devices')
class DevicesResource(Resource):
    @devices_ns.marshal_list_with(device_model)
    def get(self):
        logger.logger.info(f"Requesting all the devices")
        """Get Devices"""
        return Device.query.all()

    @devices_ns.marshal_with(device_model)
    @devices_ns.expect(device_model)
    def post(self):
        """Create a Device"""
        logger.logger.info(f"Initializing post devices")
        data = request.get_json()

        component_name = data.get('name')
        db_component= Device.query.filter_by(name=component_name).first()

        component_mem = data.get("mem_free")

        if db_component is not None:
            logger.logger.info(f"The device that was trying to create already exist")
            return jsonify({"response":"Device already exist"})
        
        if component_mem < 0 or component_mem > 100:
            logger.logger.info(f"The value for free memory is wrong {component_mem}")
            return jsonify({"response":"The value for free memory is wrong"})
        

        if data.get("cpu_utiization") < 0 or data.get("cpu_utiization") > 100:
            return jsonify({"response":"The value of the cpu_utilization must be between 0-100"})
        
        new_device = Device(
            client_count=data.get("client_count"),
            cpu_utiization=data.get("cpu_utiization"),
            firmware_version=data.get("firmware_version"),
            labels=data.get("labels"),
            macaddr=data.get("macaddr"),
            mem_free=data.get("mem_free"),
            mem_total=data.get("mem_total"),
            model=data.get("model"),
            name=data.get("name"),
            serial=str(uuid.uuid4()),
            stack_id=data.get("stack_id"),
            status=data.get("status"),
            temperature=data.get("temperature"),
            uptime=data.get("uptime"),
            uplink_ports=data.get("uplink_ports"),
            components_id=data.get("components_id")
        )

        new_device.save()

        logger.logger.info(f"New devices was created {data.get('name')}")
        return new_device, 201


@devices_ns.route('/device/<int:id>')
class DeviceResource(Resource):
    @devices_ns.marshal_with(device_model)
    def get(self,id):
        """Get devives"""
        logger.logger.info('Requesting option to get a device was iniazilizing')
        device=Device.query.get_or_404(id)

        logger.logger.info(f'Device found {device}')
        return device

    
    @devices_ns.marshal_list_with(device_model)
    @devices_ns.expect(device_model)
    def put(self, id):
        """Update the information"""
        logger.logger.info("Initialzing put for new device")
        data = request.get_json()

        device_name = data.get('name')
        db_component= Device.query.filter_by(name=device_name).first()
        
        if db_component is not None:
            logger.logger.info("Device already exist")
            return jsonify({"response":"Device already exist"})
        
        if data.get("mem_free") < 0 or data.get("mem_free") > 100:
            logger.logger.info(f"The value for free memory is wrong {data.get('mem_free')}")
            return jsonify({"response":"The value for free memory is wrong"})
        
        if data.get("cpu_utiization") < 0 or data.get("cpu_utiization") > 100:
            logger.logger.info(f"The value for cpu_utiization is wrong {data.get('cpu_utiization')}")
            return jsonify({"response":"The value of the cpu_utilization must be between 0-100"})
        
        device_to_update = Device.query.get_or_404(id)

        device_to_update.update(
            client_count=data.get("client_count"),
            cpu_utiization=data.get("cpu_utiization"),
            firmware_version=data.get("firmware_version"),
            labels=data.get("labels"),
            macaddr=data.get("macaddr"),
            mem_free=data.get("mem_free"),
            model=data.get("model"),
            stack_id=data.get("stack_id"),
            status=data.get("status"),
            temperature=data.get("temperature"),
            uptime=data.get("uptime"),
            uplink_ports=data.get("uplink_ports")
        )

        logger.logger.info(f"Device updated successfully {device_to_update}")
        return device_to_update
    

    @devices_ns.marshal_list_with(device_model)
    def delete(self, id):
        """Delete the device"""
        logger.logger.info(f"Initializing request to dele a device {id}")
        device_to_delete = Device.query.get_or_404(id)
        
        if not device_to_delete:
            logger.logger.info(f"Device with {id} does not exist")
            return jsonify({"response":"not founded"})

        device_to_delete.delete()


        logger.logger.info(f"Device {id} successfully deleted")
        return device_to_delete
    

