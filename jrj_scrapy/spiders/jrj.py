# -*- coding: utf-8 -*-
import scrapy, json
from ..items import JrjScrapyItem
from ..pipelines import JrjScrapyPipeline, STARTPAGE, PAGESIZE, ENDPAGE


class JrjSpider(scrapy.Spider):
    name = 'jrj'
    allowed_domains = ['jrj.com.com.cn']
    start_url = 'https://sso.jrj.com.cn/sso/entryRetrievePwdMobile'
    start_page = STARTPAGE
    list_403 = []   # 403结果
    pipeline = JrjScrapyPipeline()

    def start_requests(self):

        data_null = False

        while not data_null:
            phones = self.pipeline.get_phone(self.start_page)

            if len(phones) != 0 and self.start_page < ENDPAGE:  # 数据库结果非空
                self.start_page = self.start_page + 1  # 翻页

                for mobile in phones:
                    # 筛选有效数据
                    if mobile == "" or mobile[0] != "1" or len(mobile) != 11 or mobile[1] not in ["3", "5", "7", "8",
                                                                                                  "9"]:
                        continue
                    else:
                        yield scrapy.FormRequest(
                            url=self.start_url,
                            formdata={'mobile': mobile, 'verifyCode': '1'},
                            meta={"mobile": mobile, "retry": False},
                            callback=self.parse,
                        )

            else:
                data_null = True
                print("\n数据库读取完毕！%s, %s, %s\n" % (self.start_page, PAGESIZE, ENDPAGE))

    def parse(self, response):
        status_code = response.status   # 响应码
        mobile = response.meta["mobile"]    # 接收参数
        item = JrjScrapyItem()

        if status_code == 200:
            result = json.loads(response.text)

            if result["resultCode"] == "4":
                print(mobile, result)

                item["phone"] = mobile

                yield item

            else:
                # print(mobile, status_code)
                pass

        elif status_code == 403:
            # print(mobile, status_code, "重新请求")
            yield scrapy.FormRequest(
                url=self.start_url,
                formdata={'mobile': mobile, 'verifyCode': '1'},
                meta={"mobile": mobile, "retry": True},
                callback=self.parse,
                dont_filter=True,
            )

