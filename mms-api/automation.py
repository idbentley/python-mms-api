from mms_client import username, api_key, base_uri
from mms_client.automation_config import AutomationConfig
from mms_client.helpers import accept_json_header

import requests
from requests.auth import HTTPDigestAuth
import json

class Automation(object):

	def get_config(group_id):
		uri = "/api/public/v1.0/groups/{group_id}/automationConfig"
		full_uri = base_uri + uri
		full_uri = full_uri.format(group_id=group_id)
		resp = requets.get(full_uri, auth=HTTPDigestAuth(username, api_key))
		return AutomationConfig.parse_json(resp.json())

	def update_config(group_id, config):
		uri = "/api/public/v1.0/groups/{group_id}/automationConfig"
		full_uri = base_uri + uri
		full_uri = full_uri.format(group_id=group_id)
		resp = requets.post(
			full_uri,
			headers=[accept_json_header],
			data=config.to_json,
			auth=HTTPDigestAuth(username, api_key))
		return resp.status == 202

	def get_status(group_id):
		uri = "/api/public/v1.0/groups/{group_id}/automationStatus"
		full_uri = base_uri + uri
		full_uri = full_uri.format(group_id=group_id)
		resp = requets.get(full_uri, auth=HTTPDigestAuth(username, api_key))
		status = json.parse(resp.json())
		return status
