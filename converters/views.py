from django.shortcuts import render, redirect

from .functions import binaryToDecimalFunction, decimalToBinaryFunction, binaryToHexadecimalFunction, numberToTextFunction, text_binary, zeckendorf_representation_function
import re

from useful_funcs.error_msg import set_error_msg, unset_error_msg

# Create your views here.
def binToDec(request):
    if request.method == 'POST':
        binary = request.POST['binary']
        if re.match("^[01]+$", binary) == None:
            print("Binary can only contain 0's and 1's")
            request = set_error_msg(request,"Binary can only contain 0's and 1's")
            return redirect('binToDec')
            

        decimal = binaryToDecimalFunction.binToDec(binary)
        print(decimal)
        return render(request,'converters/binToDec.html', {"decimal":decimal,"input":binary})
    else:
        print(request.session.get('error_msg'))
        if request.session.get('error_msg') != "":
            error_msg = request.session.get('error_msg')
            request = unset_error_msg(request)
        else:
            error_msg = None

        return render(request, 'converters/binToDec.html',{"error_msg":error_msg})

def decToBin(request):
    if request.method == 'POST':
        decimal = request.POST['decimal']
        binary = decimalToBinaryFunction.decToBin(decimal)
        print(binary)
        return render(request,'converters/decToBin.html', {"binary":binary,"input":decimal})
    else:
        return render(request, 'converters/decToBin.html')

def binToHex(request):
    if request.method == 'POST':
        binary = request.POST['binary']
        hexadecimal = binaryToHexadecimalFunction.binToHex(binary)
        print(hexadecimal)
        return render(request,'converters/binToHex.html', {"hexadecimal":hexadecimal,"input":binary})
    else:
        return render(request, 'converters/binToHex.html')

def numberToZeckendorf_representation(request):
    if request.method == 'POST':
        positive_integer = request.POST['positive_integer']
        zeckendorf_representation_out = zeckendorf_representation_function.zeckendorf_representation(positive_integer,' ')
        
        return render(request,'converters/zeckendorf.html', {"zeckendorf_representation":zeckendorf_representation_out,"input":positive_integer})
    else:
        return render(request, 'converters/zeckendorf.html')

def textToBinary(request):
    if request.method == 'POST':
        text_input = request.POST['text']
        binary_output = text_binary.textToBin(text_input)

        return render(request,'converters/textToBinary.html', {"binary":binary_output,"input":text_input})
    else:
        return render(request, 'converters/textToBinary.html')

def binaryToText(request):
    if request.method == 'POST':
        binary_input = request.POST['binary']
        text_output = text_binary.binToText(binary_input)

        return render(request,'converters/binaryToText.html', {"text":text_output,"input":binary_input})
    else:
        return render(request, 'converters/binaryToText.html')

def numberToText(request):
    if request.method == 'POST':
        number = request.POST['number']
        # dash select doesnt work for now, deprecated
        # with_dash = request.POST['dash_select']
        # print(with_dash)
        # if with_dash == "True":
        #     with_dash = True
        # else:
        #     with_dash = False
        with_dash = False
        text_output = numberToTextFunction.numberToText(number,with_dash)
        return render(request,'converters/numberToText.html', {"text":text_output,"input":number,"dash_select":with_dash})
    else:
        return render(request, 'converters/numberToText.html')