import pandas as pd
import numpy as np

class ev_trainer():
    def __init__(self, name, item, pkrus=True):
        '''Initial class ev_trainer:
        name: pokemon's name
        item: pokemon's ev traning item, take effect if is in ['hp', 'atk', 'def', 'spa', 'spd', 'spe']
        pkrus: Whether pokemon have pkrus activate or not, default is True
        ev_spread: pandas series to store ev values'''
        
        self.name = name
        self.item = item
        self.pkrus = pkrus
        self.ev_spread = pd.Series(index=['hp', 'atk', 'def', 'spa', 'spd', 'spe'], data=[0]*6)
        self.trained = []
        self.full_ev = False
        
    def status(self):
        '''Function to print pokemon status include name, item, pkrus, current ev'''
        
        print('********************************************')
        print('name:', self.name)
        print('item:', self.item)
        print('pkrus:', self.pkrus)
        print('current ev: (Trained {} times)'.format(len(self.trained)))
        print(self.ev_spread)
        print('Total:', np.sum(self.ev_spread))
        print('********************************************')
    
    def train(self, op, base=2, pr=True):
        '''Function used to train pokemon, input:
        op: opponent, currently only support ev yield of the opponent
            have to be within ['hp', 'atk', 'def', 'spa', 'spd', 'spe']
        base: base point yield by defeating that pokemon, default = 2
        pr: print status or not, default=True'''
        
        # Check if ev is full or not
        if not self.full_ev:
            if self.pkrus == True:
                pkr = 2
            else:
                pkr = 1
        
            self.update_ev(op, base*pkr)
            
            if not self.full_ev:
                if self.item in ['hp', 'atk', 'def', 'spa', 'spd', 'spe']:
                    self.update_ev(self.item, 8*pkr)
        
        self.trained.append(op)
        
        if pr:
            print('{} finished one {} training with base {} ev'.format(self.name, op, base))
            print('current ev: (Trained {} times)'.format(len(self.trained)))
            print(self.ev_spread)
            print('\n')
    
    
    def update_ev(self, ev, value):
        '''Function to update value amount of ev to ev stats, ev have to be in ['hp', 'atk', 'def', 'spa', 'spd', 'spe']'''
        
        total = np.sum(self.ev_spread)
        pr_tot = total + value
        pr_ev = self.ev_spread[ev] + value
        if pr_tot <= 510 and pr_ev <= 252:
            self.ev_spread[ev] += value
        else:
            self.ev_spread[ev] += np.min([510 - total, 252 - self.ev_spread[ev]])
        
        if np.sum(self.ev_spread) >= 510:
            self.full_ev = True
        
    def clear(self, how='all', amount=1, value = 10):
        '''Clear pokemon's ev, take input:
        how: how to delete, can be 'all' or specific stats in ['hp', 'atk', 'def', 'spa', 'spd', 'spe']
        amount: if how is one specfic stats, assuming you are using berries, select amount of berries your pokemon is eating
        value: value of ev reduced per berry, default is 10'''
        
        if how == 'all':
            self.ev_spread = pd.Series(index=['hp', 'atk', 'def', 'spa', 'spd', 'spe'], data=[0]*6)
        elif how in self.ev_spread.index:
            self.ev_spread[how] -= amount * value
            if self.ev_spread[how] <= 0:
                self.ev_spread[how] = 0
            
    def change_item(self, item):
        '''function used to change item'''
        self.item = item
    
    def cont_train(self, opl, base=2):
        ''' For continue training, support same base point only, default = 2
        input is a list of traning opponent for pokemon to train automatically one by one, print status after the last opponent
        from opponent list opl'''
        
        for i, op in enumerate(opl):
            pr = False
            if i == len(opl)-1:
                pr = True
            self.train(op, base, pr=pr)
            
    def start_training(self):
        '''Interactive function to help fast training versus various opponent, 
        only support base point = 2 opponent for fast finishing
        IMO best used when trying to quickly max out 2 stats within same range (e.g. Route 7 for atk and spd)'''
        
        print('You entered continuous training mode with {}'.format(self.name))
        comd = 'a'
        while comd != 'q':
            self.status()
            print('Pick your opponent (choose number with keyboard):')
            print('1. Hp   2. Atk   3. Def   4. Spa   5. Spd   6. Spe   7. Change item')
            comd = input()
            if comd == '7':
                self.item = input('Enter training item or None: ')
            cmd_dict = {'1': 'hp', '2': 'atk', '3': 'def', '4': 'spa', '5': 'spd', '6': 'spe'}
            if comd in cmd_dict.keys():
                self.train(cmd_dict[comd], pr=False)