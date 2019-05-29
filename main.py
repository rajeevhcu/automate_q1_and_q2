import requests
import json
import csv

from src import logger

log = logger.get_logger(__name__)


def generate_report(url):
    with open("data/Q1&Q2.csv", "r") as fp:
        company_info = fp.readlines()

    company_info = [j.strip("\n") for j in company_info]

    with open("report.csv", "a+") as fp:
        writer = csv.writer(fp)
        # head = [j.strip('"') for j in company_info[0].split('",')]
        # heading = [head[0], head[1], head[2], "summary_level", "contextual_level"]
        # writer.writerow(heading)

        for info in company_info[567:]:
            info = [j.strip('"') for j in info.split('",')]
            row = [info[0], info[1], info[2], 0, 0]
            data1 = {"company_info": {"ticker": info[0], "perm_id": info[1], "name": info[2]},
                     "filters": {"last_days": 180}, "dataLevel": "corpus_level"}
            data2 = {"company_info": {"ticker": info[0], "perm_id": info[1], "name": info[2]},
                     "filters": {"last_days": 180}, "from": 0, "size": 10,
                     "sort_field": "content_published_date", "sort_by": "desc",
                     "dataLevel": "concept_level"}
            summary_level = [data1, data2]
            for index, level in enumerate(summary_level):
                payload = json.dumps(level)
                try:
                    log.info("request : {}".format(payload))
                    response = requests.post(url, data=payload)
                    log.info("response : {}".format(response.text))
                    log.info("status code : {}".format(response.status_code))
                    if response.status_code == 200:
                        if "summary" in response.json()["data"].keys() and response.json()["data"]["summary"] != []:
                            row[3 + index] = 1
                        else:
                            row[3 + index] = 0
                    else:
                        row[3 + index] = "response status_code : {}".format(response.status_code)
                except Exception as e:
                    log.error("error : {}".format(e))
                    row[3 + index] = "error : {}".format(e)
            writer.writerow(row)


if __name__ == "__main__":
    url = "https://api.ci.decooda.com/api/analytics/v2.0/summary?access_token=ab4ca7d8-631f-4cf0-907e-cf2a362445ad"
    generate_report(url)
