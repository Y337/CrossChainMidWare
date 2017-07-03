# coding: utf-8

def error_response(msg, code=40999):
    return {
        'error_code': code,
        'error_message': msg,
    }

# 错误码使用5-6位正整数

def mismatched_parameter_type(v, t):
    return error_response(u'%s should be stored in %s.' % (v, t), 40001)
