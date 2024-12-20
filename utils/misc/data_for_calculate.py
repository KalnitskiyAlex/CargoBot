"""позиции в кортеже: (х: USD/кг по инвойсу - начало диапазона (строго >), y: USD/кг по инвойсу - конец диапазона
(< или =), z: страховой тариф)"""

insurance_tax_list = [(0, 20, 0.01), (20, 30, 0.02), (30, 1000, 0.03)]

"""позиции в кортеже: (x: кг/м3 - начало диапазона (строго >), y: кг/м3 -конец диапазона (< или =), z: USD/кг если 
менее 5.0 / USD/м3 если более 200)"""

dishes_appliances_materials_list = [(0, 100, 300), (100, 110, 2.8), (110, 120, 2.7), (120, 130, 2.6), (130, 140, 2.5),
                                    (140, 150, 2.4),
                                    (150, 160, 2.3), (160, 170, 2.2), (170, 180, 2.1), (180, 190, 2.0), (190, 200, 1.9),
                                    (200, 250, 1.8),
                                    (250, 300, 1.7), (300, 350, 1.6), (350, 400, 1.5), (400, 500, 1.4), (500, 600, 1.3),
                                    (600, 800, 1.2),
                                    (800, 1000, 1.1), (1000, 10000, 0.8)]

"""позиции в кортеже: (x: кг/м3 - начало диапазона (строго >), y: кг/м3 -конец диапазона (< или =), z: USD/кг если 
менее 5.0 / USD/м3 если более 200)"""

household_goods_list = [(0, 100, 400), (100, 110, 3.6), (110, 120, 3.5), (120, 130, 3.3), (130, 140, 3.2),
                        (140, 150, 3.1), (150, 160, 3.0), (160, 170, 2.9), (170, 180, 2.8), (180, 190, 2.7),
                        (190, 200, 2.6), (200, 250, 2.8), (250, 300, 2.7), (300, 350, 2.6), (350, 400, 2.5),
                        (400, 500, 2.4), (500, 600, 2.3), (600, 800, 2.2), (800, 1000, 2.1), (1000, 10000, 2.2)]

"""позиции в кортеже: (x: кг/м3 - начало диапазона (строго >), y: кг/м3 -конец диапазона (< или =), z: USD/кг если 
менее 5.0 / USD/м3 если более 200)"""

shoes_clothes_list = [(0, 110, -1), (110, 120, 4.6), (120, 130, 4.5), (130, 140, 4.4), (140, 150, 4.3), (150, 160, 4.2),
                      (160, 170, 4.1), (170, 180, 4.0), (180, 190, 3.9), (190, 200, 3.8), (200, 300, 3.6),
                      (300, 400, 3.4), (400, 10000, 3.3)]

"""позиции в кортеже: (x: кг/м3 - начало диапазона (строго >), y: кг/м3 -конец диапазона (< или =), z: USD/кг если 
менее 5.0 / USD/м3 если более 200)"""

toys_list = [(0, 110, 210), (110, 120, 220), (120, 130, 230), (130, 140, 240), (140, 150, 250), (150, 160, 260),
             (160, 170, 270), (170, 180, 280), (180, 190, 290), (190, 200, 300), (200, 10000, 1.7)]