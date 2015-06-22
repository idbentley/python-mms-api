from mms_client import username, api_key, base_uri
from mms_client.automation_config import AutomationConfig
from mms_client.helpers import accept_json_header

import requests
from requests.auth import HTTPDigestAuth
import json

class Backup(object):

	def get_config(group_id, cluster_id):
		uri = "/api/public/v1.0/groups/{group_id/backupConfigs/{cluster_id}"
		full_uri = base_uri + uri
		full_uri = full_uri.format(group_id=group_id, cluster_id=cluster_id)
		resp = requets.get(full_uri, auth=HTTPDigestAuth(username, api_key))
		return BackupConfig.parse_json(resp.json())

	def patch_config(group_id, cluster_id, config):
		uri = "/api/public/v1.0/groups/{group_id/backupConfigs/{cluster_id}"
		full_uri = base_uri + uri
		full_uri = full_uri.format(group_id=group_id, cluster_id=cluster_id)
		resp = requets.patch(
			full_uri,
			headers=[accept_json_header],
			data=config.to_json,
			auth=HTTPDigestAuth(username, api_key))
		return resp.status == 202
