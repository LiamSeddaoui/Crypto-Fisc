#!/usr/bin/env.python3
# coding:utf-8
import argparse
from utils import Couleur
from datetime import datetime
import csv

parser = argparse.ArgumentParser(
    description="Tool for calculate your taxes state on your benefits of crypto investment")

parser.add_argument("-d", dest="deposit", help="add values",
                    required=False)
parser.add_argument("-w", dest="withdraw", help="withdraw values",
                    required=False)
parser.add_argument("-f", dest="fee", help="show taxes state",
                    required=False)
parser.add_argument("-r", dest="reset", help="reset value",
                    required=False)
args = parser.parse_args()


if args.deposit:
    print("\n" + str(datetime.now()))
    print(Couleur.VERT + "{*} Add values invest " + Couleur.FIN + Couleur.VIOLET + args.deposit + Couleur.FIN + "\n")
    with open('deposit.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([str(datetime.now()), args.deposit])

if args.withdraw:
    print("\n" + str(datetime.now()))
    print(Couleur.ORANGE + "{*} add value withdraw : " + Couleur.FIN + Couleur.VIOLET + args.withdraw + Couleur.FIN + "\n")
    with open('withdraw.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([str(datetime.now()), args.withdraw])

if args.fee:
    print("\n" + str(datetime.now()))
    print(Couleur.VERT + "Crypto tax calculation in progress... " + Couleur.FIN + "\n")
    with open("deposit.csv") as fin:
        deposit = sum(int(r[1]) for r in csv.reader(fin))
        print(Couleur.ORANGE + "{*} Your total crypto invest : " + Couleur.FIN + str(deposit) + "\n")
    with open("withdraw.csv") as fin:
        withdraw = sum(int(r[1]) for r in csv.reader(fin))
        print(Couleur.ORANGE + "{*} Your total crypto withdraw : " + Couleur.FIN + str(withdraw) + "\n")

    if withdraw > deposit:
        taxamount = withdraw - deposit
        tax = (taxamount * 30) / 100
        print("\n" + "Your tax for benefits crypto are : " + Couleur.ROUGE + str(tax) + " " + Couleur.FIN + "EUROS")
    else:
        print(Couleur.VERT + "Its's OK ! Actually you have not tax" + Couleur.FIN)
