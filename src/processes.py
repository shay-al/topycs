
def list_proc(name='',format='csv'):
    import subprocess as sp
    sopen=sp.Popen
    file=r'c:\temp\stream'
    with open(file,mode='w',encoding = 'utf-8') as FO:
        interact=sopen(f'tasklist /fo {format}', text=True, stdout=FO)
        interact.wait()
    with open(file,mode='r', encoding='utf-8') as FOR:
            tasks=FOR.read()
    return tasks.split("\n")

def csvproc_pid_dict(data):
    Raw=data.copy()
    Headers, Processes = Raw[0].replace("\"","").split(","), Raw[1:]

    return [{h:d for h,d in zip(Headers,proc.replace("\"","").split(","))} for proc in Processes]
    # temp={h:d for h,d in zip(Headers,Proccesses.replace("\"","").split(","))}
    # # print(temp) 
    # losy=temp.copy() 
    # del(losy['PID'])
    # return {temp['PID']:losy}

def main():
    # from processes import *
    #procs=list_proc()
    D=csvproc_pid_dict(list_proc())
    _ =[print(f'{proc["PID"]}: {str(proc)}') for proc in D]
if __name__ =='__main__':
     main()

