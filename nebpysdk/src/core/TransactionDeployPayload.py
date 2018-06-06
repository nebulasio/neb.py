# -*- coding: utf-8 -*-
# @Time    : 2018/6/3 下午9:27
# @Author  : GuoXiaoMin
# @File    : TransactionDeployPayload.py
# @Software: PyCharm
from nebpysdk.src.core.TransactionPayload import TransactionPayload
import json


class TransactionDeployPayload(TransactionPayload):


    SourceTypeJavaScript = "js"

    SourceTypeTypeScript = "ts"

    def __init__(self, sourceType,  source, args):
        self.checkArgs(sourceType, source, args);
        self.SourceType = sourceType
        self.Source = source
        self.Args = args

    def checkArgs(self ,sourceType, source, args):
        if  source == None or source.length() == 0:
            raise  Exception("invalid source of deploy payload")

        if self.SourceTypeJavaScript != sourceType and  self.SourceTypeTypeScript != sourceType:
            raise Exception("invalid source type of deploy payload")


        if args != None and args.length() > 0:
            str_json = json.loads(args)

    def getSourceType(self):
        return  self.SourceType

    def setSourceType(self, sourceType):
        self.SourceType = sourceType

    def getSource(self):
        return self.Source

    def setSource(self, Source):
        self.Source = Source

    def getArgs(self):
        return self.Args

    def setArgs(self, Args):
        self.Args = Args

    def to_bytes(self):
        return json.dumps(self)

    def gas_count(self):
        return 60
