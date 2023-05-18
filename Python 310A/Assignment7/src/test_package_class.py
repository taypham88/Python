
import package_class as pc
import unittest
import datetime as dt

class TestFunctions(unittest.TestCase):
    
    def test_assign_id(self):
        self.assertEqual(pc.assign_id(), 1004)
        
    def test_package_class(self):
        
        test = pc.Package('James Smith', 'Package', False, 5, 5, '2021-12-30', False)
        self.assertEqual(test.name,'James Smith')
        self.assertEqual(test.description,'Package')
        self.assertEqual(test.dangerous, False)
        self.assertEqual(test.weight, 5)
        self.assertEqual(test.volume, 5)
        self.assertEqual(test.big, False)
        self.assertEqual(test.required_date, dt.datetime.strptime('2021-12-30', '%Y-%m-%d').date())
        self.assertEqual(test.urgent, False)
        self.assertEqual(test.international, False)
        self.assertEqual(test.route, "Truck")
        self.assertEqual(test.cost, 25)
        
        test = pc.Package('James Smith', 'Package', True, 5, 5, '2021-12-30', False)
        self.assertEqual(test.name,'James Smith')
        self.assertEqual(test.description,'Package')
        self.assertEqual(test.dangerous, True)
        self.assertEqual(test.weight, 5)
        self.assertEqual(test.volume, 5)
        self.assertEqual(test.big, False)
        self.assertEqual(test.required_date, dt.datetime.strptime('2021-12-30', '%Y-%m-%d').date())
        self.assertEqual(test.urgent, False)
        self.assertEqual(test.international, False)
        self.assertEqual(test.route, "Truck")
        self.assertEqual(test.cost, 25)

        test = pc.Package('James Smith', 'Package', False, 5, 5, '2021-12-30', True)
        self.assertEqual(test.name,'James Smith')
        self.assertEqual(test.description,'Package')
        self.assertEqual(test.dangerous, False)
        self.assertEqual(test.weight, 5)
        self.assertEqual(test.volume, 5)
        self.assertEqual(test.big, False)
        self.assertEqual(test.required_date, dt.datetime.strptime('2021-12-30', '%Y-%m-%d').date())
        self.assertEqual(test.urgent, False)
        self.assertEqual(test.international, True)
        self.assertEqual(test.route, "Ocean")
        self.assertEqual(test.cost, 30)
        
        test = pc.Package('Tay Pham', 'New Text', False, 8, 5, '2021-12-30', True)
        self.assertEqual(test.name,'Tay Pham')
        self.assertEqual(test.description,'New Text')
        self.assertEqual(test.dangerous, False)
        self.assertEqual(test.weight, 8)
        self.assertEqual(test.volume, 5)
        self.assertEqual(test.big, True)
        self.assertEqual(test.required_date, dt.datetime.strptime('2021-12-30', '%Y-%m-%d').date())
        self.assertEqual(test.urgent, False)
        self.assertEqual(test.international, True)
        self.assertEqual(test.route, "Ocean")
        self.assertEqual(test.cost, 30)
        
        test = pc.Package('Tay Pham', 'New Text', False, 5, 5, '2021-12-15', False)
        self.assertEqual(test.name,'Tay Pham')
        self.assertEqual(test.description,'New Text')
        self.assertEqual(test.dangerous, False)
        self.assertEqual(test.weight, 5)
        self.assertEqual(test.volume, 5)
        self.assertEqual(test.big, False)
        self.assertEqual(test.required_date, dt.datetime.strptime('2021-12-15', '%Y-%m-%d').date())
        self.assertEqual(test.urgent, True)
        self.assertEqual(test.international, False)
        self.assertEqual(test.route, "Air")
        self.assertEqual(test.cost, 100)

        test = pc.Package('Tay Pham', 'New Text', True, 5, 5, '2021-12-15', False)
        self.assertEqual(test.name,'Tay Pham')
        self.assertEqual(test.description,'New Text')
        self.assertEqual(test.dangerous, True)
        self.assertEqual(test.weight, 5)
        self.assertEqual(test.volume, 5)
        self.assertEqual(test.big, False)
        self.assertEqual(test.required_date, dt.datetime.strptime('2021-12-15', '%Y-%m-%d').date())
        self.assertEqual(test.urgent, True)
        self.assertEqual(test.international, False)
        self.assertEqual(test.route, "Truck")
        self.assertEqual(test.cost, 45)      
        
if __name__=='__main__':
    unittest.main()
    
    
# (name, description, dangerous weight, volume, required_date, international)