class Percent():
    def __init__(self,number=None,part=None,percent=None):
            self.n=number
            self.p=part
            self.pcnt=percent
            self.inputs_list=[self.n,self.p,self.pcnt]
    def test_inputs(self):
        _cnt=0
        for i in self.inputs_list:
            if i: _cnt+=1
        if _cnt<2: return False
        return True
    def number(self,number=None):
        if isinstance(number,(int,float)):
            self.n=number
        else:
            if not self.n:
                 self.n=self.calc_whole()
            return self.n
    def percent(self,percent=None):
        if isinstance(percent,(int,float)):
            self.pcnt=percent
        else: 
            if not self.pcnt:
                self.pcnt=self.calc_pcnt()
            return self.pcnt    
    def part(self,part=None):
        if isinstance(part,(int,float)):
            self.p=part
        else:
            if not self.p:
                self.p=self.calc_part()
            return self.p
    def calc_part(self):
            #part=(percent*whole)/100
            if all([self.pcnt,self.n]):
                self.p=(self.pcnt*self.n)/100
                return self.p
            else: 
                return None
    def calc_whole(self):
            if all([self.p,self.pcnt]):
                 self.n= (100*self.p)/self.pcnt
                 return self.n
            return None
    def calc_pcnt(self):
            if all([self.p,self.n]):
                self.pcnt=(100*self.p)/self.n
                return self.pcnt
            return None
    def __str__(self):
        self.n,self.p,self.pcnt = self.calc_whole() if not self.n else self.n \
        ,self.calc_part() if not self.p else self.p \
        ,self.calc_pcnt() if not self.pcnt else self.pcnt
        return '\n'.join([f'number: {self.n}',f'part: {self.p}',f'percentage: {self.pcnt}'])
