from datetime import datetime
import random
import math

print("////BIENVENIDO AL SISTEMA DE PARQUEADEROS GALVIS////")
print("----------------------------------------------------")
camp_cars = int(input('Ingresa la cantidad de parqueaderos para carros: '))
camp_motorcycles = int(input('Ingresa la cantidad de parqueaderos para motos: '))

name_camp_cars = []
name_camp_moto = []

while len(name_camp_cars) < camp_cars:
    name_camp_cars.append({'place': str(input('Ingresa el nombre del campo del parqueadero de carro: ')), 'available': True})

while len(name_camp_moto) < camp_motorcycles:
    name_camp_moto.append({'place': str(input('Ingresa el nombre del campo del parqueadero de moto: ')), 'available': True})

cost_frac_car = 2000
cost_frac_moto = 1000

register_car = []
register_motorcycle = []

while True:
    place_free_moto = [x['place'] for x in name_camp_moto if x['available']]
    place_free_car = [x['place'] for x in name_camp_cars if x['available']]
    print('lugares disponibles:', place_free_car, place_free_moto)
    print('QUE OPCION DESEAS REALIZAR?')
    options = input('1. Registrar nuevo vehiculo\n2. Registrar salida de vehiculo:\nOpcion >: ')

    if not options.isdigit() or options not in ['1', '2']:
        print('NO SE ADMITEN LETRAS, SOLO LAS OPCIONES 1 o 2')
    else:
        if options == '1':
            type_vehicle = input('QUE TIPO DE VEHICULO DESEAS REGISTRAR?\n1. Moto\n2. Carro\nOpcion >: ')
            if type_vehicle not in ['1', '2']:
                print('NO SE ADMITEN LETRAS, SOLO LAS OPCIONES 1 o 2')
            elif type_vehicle == '1' and len(place_free_moto) > 0:
                placa = str(input('POR FAVOR INGRESA LA PLACA DEL VEHICULO >: '))
                hour_inside = datetime.now().strftime('%Y-%m-%d %H:%M')
                place_random = random.choice(place_free_moto)
                register_motorcycle.append({'place': place_random, 'placa': placa, 'hour_inside': hour_inside, 'Action': 'Entro'})
                for x in name_camp_moto:
                    if x['place'] == place_random:
                        x['available'] = False
                        print('El registro de vehiculos es el siguiente: ', register_motorcycle)
            elif type_vehicle == '2' and len(place_free_car) > 0:
                placa = str(input('POR FAVOR INGRESA LA PLACA DEL VEHICULO >: '))
                hour_inside = datetime.now().strftime('%Y-%m-%d %H:%M')
                place_random = random.choice(place_free_car)
                register_car.append({'place': place_random, 'placa': placa, 'hour_inside': hour_inside, 'Action': 'Entro'})
                for x in name_camp_cars:
                    if x['place'] == place_random:
                        x['available'] = False
                        print('El registro de vehiculos es el siguiente: ', register_car)
            else:
                if len(place_free_moto) == 0:
                    print('PARQUEADERO DE MOTOS LLENO')
                elif len(place_free_car) == 0:
                    print('PARQUEADERO DE CARROS LLENO')
        elif options == '2':
            option_cash = input('POR FAVOR DIGITE EL TIPO DE VEHICULO A COBRAR\n1. Moto\n2. Carro\nOpcion: ')
            if not option_cash.isdigit() or option_cash not in ['1', '2']:
                print('NO SE ADMITEN LETRAS, SOLO LAS OPCIONES 1 o 2')
            else:
                if option_cash == '1':
                    placa_pay = str(input('POR FAVOR DIGITE LA PLACA A COBRAR: '))
                    filtered_motorcycles = [x for x in register_motorcycle if x['placa'] == placa_pay and x['Action'] == 'Entro']
                    if not filtered_motorcycles:
                        print('LA PLACA CONSULTADA NO FUE ENCONTRADA')
                    else:
                        hour_inside = filtered_motorcycles[0]['hour_inside']
                        place_out = filtered_motorcycles[0]['place']
                        hour_now = datetime.now().strftime('%Y-%m-%d %H:%M')
                        total = datetime.strptime(hour_now, '%Y-%m-%d %H:%M') - datetime.strptime(hour_inside, '%Y-%m-%d %H:%M')
                        total = total.total_seconds()
                        total = total / 3600
                        total = math.ceil(total)
                        total = total * cost_frac_moto
                        print('Tu valor a pagar de parqueo es => ', total)
                        for x in name_camp_moto:
                            if x['place'] == place_out:
                                x['available'] = True
                        for x in register_motorcycle:
                            if x['placa'] == placa_pay:
                                x['hour_out'] = datetime.now.strftime('%Y-%m-%d %H:%M')
                                x['pay_all'] = total
                                x['Action'] = 'salio'
                        print('Los vehiculos motorizados registrados son los siguientes: ', register_motorcycle)
                elif option_cash == '2':
                    placa_pay = str(input('POR FAVOR DIGITE LA PLACA A COBRAR: '))
                    filtered_cars = [x for x in register_car if x['placa'] == placa_pay and x['Action'] == 'Entro']
                    if not filtered_cars:
                        print('LA PLACA CONSULTADA NO FUE ENCONTRADA')
                    else:
                        hour_inside = filtered_cars[0]['hour_inside']
                        place_out = filtered_cars[0]['place']
                        hour_now = datetime.now().strftime('%Y-%m-%d %H:%M')
                        total = datetime.strptime(hour_now, '%Y-%m-%d %H:%M') - datetime.strptime(hour_inside, '%Y-%m-%d %H:%M')
                        total = total.total_seconds()
                        total = total / 3600
                        total = math.ceil(total)
                        total = total * cost_frac_car
                        print('Tu valor a pagar de parqueo es => ', total)
                        for x in name_camp_cars:
                            if x['place'] == place_out:
                                x['available'] = True
                        for x in register_car:
                            if x['placa'] == placa_pay:
                                x['hour_out'] = datetime.now().strftime('%Y-%m-%d %H:%M')
                                x['pay_all'] = total
                                x['Action'] = 'salio'
                        print('Los vehiculos registrados son los siguientes: ', register_car)
                else:
                    print('POR FAVOR INTRODUZCA UNA SELECCION VALIDA')
