# -*- Coding: utf-8 -*-
# Author: heaton
# @Time: 2022/5/17 20:14
# @File: erp_mock.py

from flask import Flask,jsonify,request,render_template
import settings,time

#实例化
erp_int = Flask(__name__, template_folder="./templates")
erp_int.config.from_object(settings)

def fill_blank(fill_name,fill_content):
    if fill_name == "":
        return jsonify(
            {
                "code": 101,
                "msg": fill_content + "不能为空"
            }
        )


def choose_fill(fill_name):
    if fill_name == '' or fill_name != '':
       pass

#接口（URL，方式，参数 （header,body）,返回值）
@erp_int.route('/temdata',methods=["POST"])
def login():
    if request.method == "POST":
        uname = request.get_json()['username']
        pawd = request.get_json()['password']
        if uname == "hsw" and pawd == "123":
            return render_template('erp.json.py')
        else:
            return jsonify(
                {
                    "code": 102,
                    "msg": "密码或用户名不正确"
                }
            )
    else:
        return jsonify(
            {
                "code": 101,
                "msg":"方式不正确"
            }
        )

@erp_int.route('/erp/bill', methods = ['POST'])

def bill():
    print(request.method)
    print(request.get_json())

    if request.method == 'POST':

        id_bill = request.get_json()['id'] #必填
        fill_blank(id_bill,"订单编号")

        orderquantity = request.get_json()['orderQuantity'] #必填
        fill_blank(orderquantity,"订单方量")

        materialType = request.get_json()['materialType'] #必填
        material_list = ["C10","C15","C20","C25","C30","C35","C40","C45","C50","C55","C60","C70"]
        fill_blank(materialType,"规格型号")

        if materialType in material_list:
           pass
        else:
            return jsonify(
                {
                    "code": 104,
                    "msg": "规格型号不正确"
                }
            )

    admixtureCombination = request.get_json()['admixtureCombination']
    choose_fill(admixtureCombination)
    #
    slumps = request.get_json()['slumps']
    choose_fill(slumps)
    #
    pouringType = request.get_json()['pouringType'] #必填
    pouring_list = ['10','20','30','40']
    fill_blank(pouringType,"浇筑方式")

    if pouringType in pouring_list:
        pass
    else:
        return jsonify(
            {
                "code": 106,
                "msg":"浇筑方式不正确"
                }
            )
    #

    pumpTruckHeight = request.get_json()['pumpTruckHeight']
    pump_list = [38,46,47,48,50,52,56,60,62,63]
    fill_blank(pumpTruckHeight,"泵送高度")
    if pumpTruckHeight in pump_list:
        pass
    else:
        return jsonify(
            {
                    "code": 107,
                    "msg": "泵送高度不正确"
                    }
            )

    pourSite = request.get_json()['pourSite']
    fill_blank(pourSite,"浇筑部位")
    #
    planUseTime = request.get_json()['planUseTime']
    fill_blank(planUseTime,"预计使用时间")
    #
    memo = request.get_json()['memo']
    choose_fill(memo)
    #
    stationId = request.get_json()['stationId']
    fill_blank(stationId,"厂站编号")

    station = request.get_json()['station']
    fill_blank(station,"厂站名称")

    projectId = request.get_json()['projectId']
    fill_blank(projectId,"项目编号")

    projectName = request.get_json()['projectName']
    fill_blank(projectName,"项目名称")

    placer = request.get_json()['placer']
    fill_blank(placer,"下单人")

    orderDate = request.get_json()['orderDate']
    fill_blank(orderDate,"下单时间")

    placerPhone = request.get_json()['placerPhone']
    fill_blank(placerPhone,"下单人电话")

    return jsonify(
        {
        "add":{
            "id":request.get_json()["id"],
            "orderQuantity": request.get_json()["orderQuantity"],
            "materialType":request.get_json()["materialType"],
            "admixtureCombination": request.get_json()['admixtureCombination'],
            "slumps":request.get_json()['slumps'],
            "pouringType" : request.get_json()['pouringType'],
            "pumpTruckHeight" :request.get_json()['pumpTruckHeight'],
            "pourSite": request.get_json()['pourSite'],
            "planUseTime" :request.get_json()['planUseTime'],
            "memo" : request.get_json()['memo'],
            "stationId" : request.get_json()['stationId'],
            "station": request.get_json()['station'],
            "projectId" : request.get_json()['projectId'],
            "projectName":request.get_json()['projectName'],
            "placer":request.get_json()['placer'],
            "orderDate": request.get_json()['orderDate'],
            "placerPhone":request.get_json()['placerPhone']
    },"code":"200"
    })

@erp_int.route('/')
def index():
    return time.strftime('%Y-%m-%d_%H_%M_%S')

@erp_int.route('/post/<int:num>')
def add(num):
    result = num + 10
    return "{}号".format(int(result))

@erp_int.route('/float/<float:money>')
def add1(money):
    result = money + 10
    # print(type(result))
    return str(result)
#启动服务
if __name__ == '__main__':
    erp_int.config['JSON_AS_ASCII'] = False
    erp_int.run(host='0.0.0.0',port=50000,debug=True)