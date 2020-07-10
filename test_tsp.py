from tspp import TSP
import unittest
import  sys
from math import sqrt 
import os




class Test_all(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
            cls.positions={1: (5, 10), 2: (1, 1), 3: (10, 5), 4: (15, 7)}
            cls.start=3
            cls.object= TSP(cls.positions,cls.start)

    def test_init(self):
        init_attributes_dic=self.object.__dict__
        init_attributes=init_attributes_dic.keys()
        init_attributes=set(init_attributes)
        self.assertSetEqual(init_attributes, {'start', 'vertex_num', 'position'},'  ** __init__ function attributes are Wrong! ** ')
        print('  ** __init__ function attributes are OK ** ')


    def test_calc_distance(self):
        flag = (hasattr(self.object, 'calc_distance'))
        self.assertTrue(flag, ' ** calc_distance  method does not exist ** ')
        if flag:
             cal = self.object.calc_distance(self.positions[1],self.positions[2])
             self.assertAlmostEqual(sqrt(97),cal,msg=' ** calc_distance method calculatting two points distance is wrong!  **')
             print(' ** calc_distance method calculatting two points distance is OK ** ')
        

    def test_sequence(self):
        flag = (hasattr(self.object, 'sequence'))
        self.assertTrue(flag, ' ** test_sequence  method does not exist ** ')
        if flag:
            seq = self.object.sequence()
            seq=list(seq)
            count=len(self.positions)
            for i in seq:
                self.assertEqual(len(i),count+1,' ** Some cities visited more than one time!  **')
                self.assertSetEqual(set(i), set(self.positions.keys()), ' ** sequences do not contain all cities!  **')
            print(' ** sequences containning all cities is OK  ** \n\n ** All cities visited one time is OK  **')


    def test_seq_distance(self):
        flag = (hasattr(self.object, 'seq_distance'))
        self.assertTrue(flag, ' ** seq_distance  method does not exist ** ')
        if flag:
            seq=list(self.positions.keys())
            seq.append(1)
            dist=self.object.seq_distance(tuple(seq))
            self.assertAlmostEqual(2*sqrt(97)+sqrt(109)+sqrt(29),dist,msg=' ** seq_distance method calculating total distance is wrong! ** ')
            print(' **  seq_distance method calculating total distance is OK!  ** ')

    def test_find_min(self):
        flag = (hasattr(self.object, 'find_min'))
        self.assertTrue(flag, ' ** find_min  method does not exist ** ')
        if flag:
            seq=self.object.sequence()
            dis,p=self.object.find_min(seq)
            self.assertAlmostEqual(2*sqrt(97)+sqrt(109)+sqrt(29),dis,msg=' ** find_min method finding shortest path is wrong! ** ')
            print(f'Shortest path length is : {dis}')
            print('** Congadulations You found Shortest path **')


