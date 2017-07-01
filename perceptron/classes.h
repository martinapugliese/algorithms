/**********************
        CLASSES
***********************/


class Neuron {

public:

    signed int bias;
    int sum;

    void setBias(int t) {
        bias = - t;
    };

    int computeOutput(int * inputs, int * weights) {
        sum = 0;
        for(i=0;i<N;i++)
            sum += weights[i] * inputs[i];

        if(sum <= - bias)
            return 0;
        else
            return 1;
    }

};
