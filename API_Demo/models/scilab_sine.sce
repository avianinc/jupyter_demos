// fetch arguments
args=sciargs()
disp(args)

// load the blocks library and the simulation engine
loadXcosLibs(); loadScicos();

importXcosDiagram("C:/Users/jdehart/Documents/GitHub/jupyter_demos/API_Demo/models/scilab_sine.zcos")

typeof(scs_m) //The diagram data structure

//This diagram uses 3 context variables : 
//  Amplitude : the sin function amplitude
//  Pulsation : the sin function pulsation
//  Tf        : the final simulation time
scs_m.props.context; //the embedded definition

// Simulate the model
Context.Amp=1;
Context.Freq=10;
scicos_simulate(scs_m,list(),Context,'nw');

// plot A
plot(A.values);
