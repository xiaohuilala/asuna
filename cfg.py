# -*- coding: utf-8 -*-# 
#-------------------------------------------------------------------------------
# Name:         cfg
# Description:  
# Author:       wujian
# Date:         2019/11/9
#-------------------------------------------------------------------------------
import requests
from pprint import pprint

email = "wujian@ones.ai"
password = "wujian8808"
project_public_url = "https://api.ones.ai/project/v1"
pro_project_public_url = "https://api.ones.ai/project/api/project/"

close = "QXSKmnQQ" #"关闭"状态的uuid
solve = "7YWLTyfY" #"确认解决"状态的uuid
bug_type = "DLMM2DJD"  #反馈状态为bug的任务类型
demand_type = "5HiaccVH"#反馈状态为新需求的任务类型

types = ["DLMM2DJD","5HiaccVH"]





Testrobot_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=5b960cb3-f2a9-49b7-98fa-bb6506b05d19"
True_Robot_url ="https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=0b3cb60b-4868-43ef-a185-e5f4ad46078c"
