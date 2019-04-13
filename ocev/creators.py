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

class OperatorCreator():
    types = {'bin':op.BinaryOperator,
            'int':op.IntegerOperator,
            'int-perm':op.PermutedIntegerOperator,
            'real':op.RealOperator}

    @staticmethod
    def get_operator(cod):
        return OperatorCreator.types[cod]()