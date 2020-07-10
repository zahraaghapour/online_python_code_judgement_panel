import math
import  random
class TSP:
    def __init__(self,position,start):
        self.vertex_num=len(position)
        self.start=start
        self.position=position

    def calc_distance(self,p1,p2):
        dis=((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2)
        distance=math.sqrt(dis)
        return(distance)

    def sequence(self):
        total_seq=set()
        while len(total_seq) !=(math.factorial((self.vertex_num)-1)):
            seq=[]
            s=self.start
            while len(seq)!=(self.vertex_num)  :
                while s in seq:
                    s=random.randint(1, self.vertex_num)
                seq.append(s)
                s = random.randint(1, self.vertex_num)
            seq.append(self.start)
            x=tuple(seq)
            total_seq.add(x)

        return  total_seq

    def seq_distance(self,seq):
        sum_distance=0
        for i in range((self.vertex_num)):
            p1=seq[i]
            p2 = seq[i+1]
            dist = self.calc_distance(self.position[p1],self.position[p2])
            p1 = p2
            sum_distance = dist+sum_distance
        return sum_distance

    def find_min(self,total_seq):
        total_seq=list(total_seq)
        min=self.seq_distance(total_seq[0])
        answer=total_seq[0]
        for i in total_seq:
            if self.seq_distance(i)<min:
                min=self.seq_distance(i)
                answer=i
        return min , answer

