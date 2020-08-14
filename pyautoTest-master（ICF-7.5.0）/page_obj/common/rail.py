from testrail import *
import time
import pprint


# testrail testrun id
test_run_id = 410


def rail_pass(runid, caseid):

	client = APIClient('http://10.1.1.151/testrail/')
	# client = APIClient('http://http://bmdwq.tpddns.cn:18082/testrail/')
	client.user = 'swy@baomutech.com'
	client.password = 'Ars25342648!'
	# case = client.send_get('get_results_for_run/178')
	# pprint.pprint(case)
	try:
		result = client.send_post(
			'add_result_for_case/' + str(runid) + '/'+str(caseid),
			{ 'status_id': 1, 'comment': 'This test worked fine! -- by pytest\n' + time.ctime()})
	except:
		print("\ntestrail_pass执行失败，请检查testrail连通性、runid、caseid")

def rail_block(runid, caseid):

	client = APIClient('http://10.1.1.151/testrail/')
	client.user = 'swy@baomutech.com'
	client.password = 'Ars25342648!'
	# case = client.send_get('get_results_for_run/178')
	# pprint.pprint(case)

	result = client.send_post(
		'add_result_for_case/' +str(runid)+ '/'+str(caseid),
		{ 'status_id': 2, 'comment': 'This test worked fine! -- by pytest\n'+ time.ctime() })


def rail_retest(runid, caseid):

	client = APIClient('http://10.1.1.151/testrail/')
	client.user = 'swy@baomutech.com'
	client.password = 'Ars25342648!'
	# case = client.send_get('get_results_for_run/178')
	# pprint.pprint(case)

	result = client.send_post(
		'add_result_for_case/' +str(runid)+ '/'+str(caseid),
		{ 'status_id': 4, 'comment': 'This test worked fine! -- by pytest\n'+ time.ctime() })


def rail_fail(runid, caseid):

	client = APIClient('http://10.1.1.151/testrail/')
	# client = APIClient('http://http://bmdwq.tpddns.cn:18082/testrail/')
	client.user = 'swy@baomutech.com'
	client.password = 'Ars25342648!'
	# case = client.send_get('get_results_for_run/178')
	# pprint.pprint(case)

	try:
		result = client.send_post(
			'add_result_for_case/' +str(runid)+ '/'+str(caseid),
			{ 'status_id': 5, 'comment': 'This test worked fine! -- by pytest\n' + time.ctime() })
	except:
		print("\ntestrail_fail执行失败，请检查testrail连通性、runid、caseid")

