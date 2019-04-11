import ocev.individual as ind
import ocev.operators as op

class IndvidualCreator():
    types = {'bin':ind.Binary,
            'int':ind.Integer,
            'int-perm':ind.PermutedInteger,
            'real':ind.Real}
    @staticmethod
    def create(cod, ind_args):
            return IndvidualCreator.types[cod](ind_args)
'''
class OperatorCreator():
    types = {'bin':op.BinaryOperator,
            'int':op.IntegerOperator,
            'int-perm':op.PermutedIntegerOperator,
            'real':op.RealOperator}
 
    def __init__(self,cod, pop, args):
        self.get_operator(cod, pop, args)

    def get_operator(self, cod, pop, args):
        return OperatorCreator.types[cod](pop, args)
'''