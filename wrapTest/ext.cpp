#include<iostream>
#include<Python.h>
#include<math.h>

static PyObject * extError;
using namespace std;
int Prime(int n)
{
    if(n<=1)
    {
        cout << "Not Prime." << endl;
        return -1;
    }
    if(n==2|n==3)
    {   
        cout<<"Is Prime."<<endl;
        return 1;
    }
    for(int i=2; i<=(int)sqrt(n); i++)
        if(n%i==0)
        {
            cout<<"Not Prime."<<endl;
            return -1;
        }
    cout <<"Is Prime." <<endl;
    return 1;
}

static PyObject* ext_Prime(PyObject *self, PyObject *args)
{
    int n = 0;
    if(!PyArg_ParseTuple(args,"i",&n)) return NULL;
    return Py_BuildValue("i",Prime(n));
}

static PyMethodDef extMethods[]={
    {"ext_Prime",(PyCFunction)ext_Prime,METH_VARARGS}, //ext_Prime is functions name
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC initext()
{
    Py_InitModule("ext",extMethods);
}

