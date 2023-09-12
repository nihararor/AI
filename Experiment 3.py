import pgmpy.models
import pgmpy.inference
from pgmpy.factors.discrete.CPD import TabularCPD
model = pgmpy.models.BayesianNetwork([('Burglary', 'Alarm'),
                                    ('Earthquake', 'Alarm'),
                                    ('Alarm', 'JohnCalls'),
                                    ('Alarm', 'MaryCalls')])
cpdburglary = TabularCPD('Burglary', 2, [[0.001] ,[0.999,]])
cpdearthquake =TabularCPD('Earthquake', 2, [[0.002], [0.998]])
cpdalarm =TabularCPD('Alarm', 2, [[0.95, 0.94, 0.29, 0.001],[0.05, 0.06, 0.71, 0.999]],
                                              evidence=['Burglary', 'Earthquake'],
                                              evidence_card=[2, 2])
cpdjohn = TabularCPD('JohnCalls', 2, [[0.90, 0.05],[0.10, 0.95]],
                                              evidence=['Alarm'],
                                              evidence_card=[2])
cpdmary = TabularCPD('MaryCalls', 2, [[0.70, 0.01],[0.30, 0.99]],
                                              evidence=['Alarm'],
                                              evidence_card=[2])
model.add_cpds(cpdburglary, cpdearthquake, cpdalarm, cpdjohn, cpdmary)
model.check_model()
print('Probability distribution, P(Burglary)')
print(cpdburglary)
print()
print('Probability distribution, P(Earthquake)')
print(cpdearthquake)
print()
print('Joint probability distribution, P(Alarm | Burglary, Earthquake)')
print(cpdalarm)
print()
print('Joint probability distribution, P(JohnCalls | Alarm)')
print(cpdjohn)
print()
print('Joint probability distribution, P(MaryCalls | Alarm)')
print(cpdmary)
print()

infer=pgmpy.inference.VariableElimination(model)
alarm_dist=infer.query(["Alarm"],evidence={'Burglary' : 0, 'Earthquake' : 1}) 
print(alarm_dist)

mary_dist=infer.query(["MaryCalls"],evidence={'Burglary' : 0, 'Earthquake' :1, 'Alarm' : 1})
print(mary_dist) 
john_dist=infer.query(["JohnCalls"],evidence={'Burglary' : 1, 'Earthquake' :0, 'Alarm' : 1})
print(john_dist)