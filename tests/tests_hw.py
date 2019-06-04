import unittest
import uuid
import objects_and_classes.homework.homework as hw

car_price_errm = "\n'Price' argument should be numeric\n"
car_mileage_errm = "\n'Mileage' argument should be numeric\n"
car_type_errm = "\nIncorrect value for 'Type' argument\n"
car_producer_errm = "\nIncorrect value for 'Producer' argument\n"

garage_places_type_errm = "\n'Places' argument should be 'int'\n"
garage_places_val_errm = "\n'Places' argument should be greater than 0\n"
garage_town_errm = "\nIncorrect value for 'Town' argument\n"
garage_cars_errm = "\nIncorrect value for 'Cars' argument\n"
garage_car_add_errm = "\nCar with id {} can not be added to more than one garage\n"
garage_free_space_errm = "\nThere is no enough free places in garage\n"
garage_car_remove_errm = "\nCar with id {} doesn`t exists in this garage\n"
garage_car_val_errm = "\nIncorrect value for 'Car' argument\n"

millionaire_add_gar_errm = "\nGarage can not be assigned to more than one owner\n"
millionaire_add_car_errm = "\n{} is not owner of this garage\n"


class CarTest(unittest.TestCase):
    def test_price_error(self):
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            car = hw.Car('99999', 'Sedan', 'BENTLEY', 1000)
        self.assertTrue(car_price_errm in context.exception.args)

    def test_mileage_error(self):
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            car = hw.Car(99999, 'Sedan', 'BENTLEY', '1000')
        self.assertTrue(car_mileage_errm in context.exception.args)

    def test_car_type_error(self):
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            car = hw.Car(99999, '????', 'BENTLEY', 1000)
        self.assertTrue(car_type_errm in context.exception.args)

    def test_producer_error(self):
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            car = hw.Car(99999, 'Sedan', '????', 1000)
        self.assertTrue(car_producer_errm in context.exception.args)

    def test_all_errors(self):
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            car = hw.Car('99999', '????', '????', '1000')
        self.assertTrue(car_price_errm + car_mileage_errm + car_type_errm + car_producer_errm in context.exception.args)

    def test_car_id_type(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        self.assertTrue(isinstance(car1.get_id(), uuid.UUID))

    def test_car_change_id(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        old_id = car1.get_id()
        car1.change_id()
        self.assertTrue(old_id != car1.get_id())

    def test_car_print(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        expected_value = "Price: $99999.0, Type: Sedan, Producer: BENTLEY, Id: {}, Mileage: 1000.0".format(
            car1.get_id())
        car_str = str(car1)
        self.assertEqual(expected_value, car_str)


class CarComparisonTest(unittest.TestCase):

    car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
    car2 = hw.Car(15000, 'Sedan', 'BMW', 10000)

    def test_car_gt_comparison(self):
        self.assertGreater(CarComparisonTest.car1, CarComparisonTest.car2)

    def test_car_ge_comparison(self):
        self.assertGreaterEqual(CarComparisonTest.car1, CarComparisonTest.car2)

    def test_car_ne_comparison(self):
        self.assertNotEqual(CarComparisonTest.car1, CarComparisonTest.car2)

    def test_car_lt_comparison(self):
        self.assertLess(CarComparisonTest.car2, CarComparisonTest.car1)

    def test_car_le_comparison(self):
        self.assertLessEqual(CarComparisonTest.car2, CarComparisonTest.car1)

    def test_car_eq_comparison(self):
        self.assertFalse(CarComparisonTest.car1 == CarComparisonTest.car2)


class GarageTest(unittest.TestCase):
    def test_places_type_error(self):
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            garage = hw.Garage("Amsterdam", 2.0, cars=None, owner=None)
        self.assertTrue(garage_places_type_errm in context.exception.args)

    def test_places_val_error(self):
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            garage = hw.Garage("Amsterdam", 0, cars=None, owner=None)
        self.assertTrue(garage_places_val_errm in context.exception.args)

    def test_town_error(self):
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            garage = hw.Garage("????", 2, cars=None, owner=None)
        self.assertTrue(garage_town_errm in context.exception.args)

    def test_cars_error_1(self):
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            garage = hw.Garage("Amsterdam", 2, cars=1, owner=None)
        self.assertTrue(garage_cars_errm in context.exception.args)

    def test_cars_error_2(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            garage = hw.Garage("Amsterdam", 2, cars=[car1, [1]], owner=None)
        self.assertTrue(garage_cars_errm in context.exception.args)

    def test_car_add_error_1(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            garage = hw.Garage("Amsterdam", 2, cars=[car1, car1], owner=None)
        self.assertTrue(
            garage_car_add_errm.format(car1.get_id()) in context.exception.args and car1.is_in_garage() is False)

    def test_car_add_error_2(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            garage = hw.Garage("Amsterdam", 2, cars=[car1], owner=None)
            garage.add(car1)
        self.assertTrue(
            garage_car_add_errm.format(car1.get_id()) in context.exception.args)

    def test_car_add_error_3(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        car2 = hw.Car(15000, 'Sedan', 'BMW', 10000)
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            garage = hw.Garage("Amsterdam", 1, cars=[car1, car2], owner=None)
        self.assertTrue(garage_free_space_errm in context.exception.args and car1.is_in_garage() is False)

    def test_car_add_error_4(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        car2 = hw.Car(15000, 'Sedan', 'BMW', 10000)
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            garage = hw.Garage("Amsterdam", 1, cars=[car1], owner=None)
            garage.add(car2)
        self.assertTrue(garage_free_space_errm in context.exception.args and car2.is_in_garage() is False)

    def test_car_add_error_5(self):
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            garage = hw.Garage("Amsterdam", 1, cars=None, owner=None)
            garage.add(1)
        self.assertTrue(garage_car_val_errm in context.exception.args)

    def test_car_remove_error_1(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        car2 = hw.Car(15000, 'Sedan', 'BMW', 10000)
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            garage = hw.Garage("Amsterdam", 1, cars=[car1], owner=None)
            garage.remove(car2)
        self.assertTrue(garage_car_remove_errm.format(car2.get_id()) in context.exception.args and car1 in garage)

    def test_car_remove_error_2(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            garage = hw.Garage("Amsterdam", 1, cars=[car1], owner=None)
            garage.remove(1)
        self.assertTrue(garage_car_val_errm in context.exception.args)

    def test_car_add(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        garage = hw.Garage("Amsterdam", 1, cars=[car1], owner=None)
        self.assertTrue(car1 in garage and car1.is_in_garage() is True)

    def test_car_remove(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        garage = hw.Garage("Amsterdam", 1, cars=[car1], owner=None)
        garage.remove(car1)
        self.assertTrue(car1 not in garage and car1.is_in_garage() is False)

    def test_hit_hat(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        car2 = hw.Car(15000, 'Sedan', 'BMW', 10000)
        expected_value = 114999
        garage = hw.Garage("Amsterdam", 2, cars=[car1, car2], owner=None)
        self.assertEqual(garage.hit_hat(), expected_value)

    def test_garage_print(self):
        garage1 = hw.Garage("Amsterdam", 1)
        expected_value = "Town: Amsterdam, Cars: 0, Places: 1, Owner: None"
        garage_str = str(garage1)
        self.assertEqual(expected_value, garage_str)


class MillionaireTest(unittest.TestCase):
    def test_garage_add_error(self):
        garage1 = hw.Garage("Amsterdam", 2)
        garage2 = hw.Garage("Kiev", 1)
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            millionaire1 = hw.Millionaire("Antony", garage1)
            millionaire2 = hw.Millionaire("Pablo", garage1)
        self.assertTrue(millionaire_add_gar_errm in context.exception.args)

    def test_car_add_error(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        garage1 = hw.Garage("Amsterdam", 2)
        garage2 = hw.Garage("Kiev", 1)
        with self.assertRaises(hw.CustomException, msg="Should occur the exception") as context:
            millionaire1 = hw.Millionaire("Antony", [garage1])
            millionaire2 = hw.Millionaire("Pablo", [garage2])
            millionaire1.add_car(car1, garage2)
        self.assertTrue(millionaire_add_car_errm.format(millionaire1.name) in context.exception.args)

    def test_car_add(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        garage1 = hw.Garage("Amsterdam", 2)
        millionaire1 = hw.Millionaire("Antony", [garage1])
        millionaire1.add_car(car1, garage1)
        self.assertTrue(car1 in garage1 and car1.is_in_garage() is True)

    def test_car_add_default_garage(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        garage1 = hw.Garage("Amsterdam", 1)
        garage2 = hw.Garage("Kiev", 10)
        garage3 = hw.Garage("Prague", 5)
        millionaire1 = hw.Millionaire("Antony", [garage1, garage2, garage3])
        millionaire1.add_car(car1)
        self.assertTrue(car1 in garage2 and car1.is_in_garage() is True)

    def test_hit_hat(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        car2 = hw.Car(15000, 'Sedan', 'BMW', 10000)
        car3 = hw.Car(10000, 'Sedan', 'BMW', 10000)
        garage1 = hw.Garage("Amsterdam", 1)
        garage2 = hw.Garage("Kiev", 2)
        expected_value = 124999
        millionaire1 = hw.Millionaire("Antony", [garage1, garage2])
        millionaire1.add_car(car1, garage1)
        millionaire1.add_car(car2, garage2)
        millionaire1.add_car(car3, garage2)
        self.assertEqual(millionaire1.hit_hat(), expected_value)

    def test_garages_count(self):
        garage1 = hw.Garage("Amsterdam", 1)
        garage2 = hw.Garage("Kiev", 2)
        expected_value = 2
        millionaire1 = hw.Millionaire("Antony", [garage1, garage2])
        self.assertEqual(millionaire1.garages_count(), expected_value)

    def test_cars_count(self):
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        car2 = hw.Car(15000, 'Sedan', 'BMW', 10000)
        car3 = hw.Car(10000, 'Sedan', 'BMW', 10000)
        garage1 = hw.Garage("Amsterdam", 1)
        garage2 = hw.Garage("Kiev", 2)
        expected_value = 3
        millionaire1 = hw.Millionaire("Antony", [garage1, garage2])
        millionaire1.add_car(car1, garage1)
        millionaire1.add_car(car2, garage2)
        millionaire1.add_car(car3, garage2)
        self.assertEqual(millionaire1.cars_count(), expected_value)

    def test_millionaire_print(self):
        expected_value = "Name: Antony, Garages: 1, Cars: 1, Total cars cost: 99999.0"
        car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
        garage1 = hw.Garage("Amsterdam", 1)
        millionaire1 = hw.Millionaire("Antony", [garage1])
        millionaire1.add_car(car1, garage1)
        millionaire_str = str(millionaire1)
        self.assertEqual(expected_value, millionaire_str)


class MillionaireComparisonTest (unittest.TestCase):
    car1 = hw.Car(99999, 'Sedan', 'BENTLEY', 1000)
    car2 = hw.Car(15000, 'Sedan', 'BMW', 10000)
    car3 = hw.Car(10000, 'Sedan', 'BMW', 10000)
    garage1 = hw.Garage("Amsterdam", 1)
    garage2 = hw.Garage("Kiev", 2)
    garage3 = hw.Garage("Prague", 5)
    expected_value = 3
    millionaire1 = hw.Millionaire("Antony", [garage1, garage2])
    millionaire2 = hw.Millionaire("Antony", [garage3])
    millionaire1.add_car(car1)
    millionaire1.add_car(car2)
    millionaire2.add_car(car3)

    def test_millionaire_gt_comparison(self):
        self.assertGreater(MillionaireComparisonTest.millionaire1, MillionaireComparisonTest.millionaire2)

    def test_millionaire_ge_comparison(self):
        self.assertGreaterEqual(MillionaireComparisonTest.millionaire1, MillionaireComparisonTest.millionaire2)

    def test_millionaire_ne_comparison(self):
        self.assertNotEqual(MillionaireComparisonTest.millionaire1, MillionaireComparisonTest.millionaire2)

    def test_millionaire_lt_comparison(self):
        self.assertLess(MillionaireComparisonTest.millionaire2, MillionaireComparisonTest.millionaire1)

    def test_millionaire_le_comparison(self):
        self.assertLessEqual(MillionaireComparisonTest.millionaire2, MillionaireComparisonTest.millionaire1)

    def test_millionaire_eq_comparison(self):
        self.assertFalse(MillionaireComparisonTest.millionaire1 == MillionaireComparisonTest.millionaire2)


if __name__ == '__main__':
    unittest.main()
