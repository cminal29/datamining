This is a project  "prediction of renewable energy consumption in states of US"


-----------------------------------------------------------------------------------

Commands to execute:

import Minal_data_harvest
obj=Minal_data_harvest.data_harvest()
extr=obj.load_data()

import Minal_data_model
process_model=Minal_data_model.data_models()
predicted_values=process_model.linear_fit()


-----------------------------------------------------------------------------------