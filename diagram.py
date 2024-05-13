
import numpy as np
import matplotlib.pyplot as plt
import math

def recovery_function(t,a,b,c,v):
    return a*(math.pow((b+c),b+c)/(math.pow(b,b)*math.pow(c,c)))*np.power(t/v,b)*np.power(1-t/v,c)

def diagram_plot(path,case):
    #fig,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,figsize=(10,8))
    fig, ax1 = plt.subplots(1, 1, figsize=(3, 2))
    duration=4
    t=np.arange(0,duration*10)
    y_target=list(map(lambda x:  x*x*0.0005-x*0.001+1, list(t)))
    y_target = np.array(y_target)


    start_t1=10;end_t1=40;v=end_t1-start_t1

    if case=='example':
        a=0.5;b=2;c=2
    if case=='example_large_magnitude':
        a=0.6;b=2;c=2
    if case=='example_late_recovery':
        end_t1 =40;
        v = end_t1 - start_t1
        a=0.5;b=2;c=3
    if case=='never_recovery':
        end_t1 =40;
        v = end_t1 - start_t1
        a=0.5;b=0.2;c=0.2


    t_MOP = np.arange(0, v)
    y_MOP_temp=list(recovery_function(t_MOP,a,b,c,v))
    print(np.max(y_MOP_temp))
    absorb_t1 = [x for x, y in zip(t, y_MOP_temp) if y == np.max(y_MOP_temp)][0]+start_t1
    y_MOP=list([0]*start_t1)+y_MOP_temp+list([0]*(duration*10-end_t1))
    print(y_MOP)

    y_MOP=y_target-y_MOP


    ax1.plot(t[start_t1:duration * 10] , y_MOP[start_t1:duration * 10], color='#f46d43', linewidth=2,
             zorder=2)  # '#f46d43'
    ax1.plot(t, y_target, color='#2c7bb6', zorder=1, linewidth=1)
    ax1.plot(t[0:absorb_t1 ] , y_target[0:absorb_t1 ] - a, color='#2c7bb6', linestyle='--', linewidth=0.5)
    ax1.fill_between(t , y_target, y_MOP, alpha=0.3, color='#fee5d9')

    max_v = np.max(y_target)
    min_v = np.min(y_target - a)

    # ax1.axvspan(0, start_t1 / 10 + 1, alpha=0.3, facecolor='#d9d9d9',zorder=0)
    ax1.fill_between(t[start_t1:absorb_t1 +1] , [0.4] * ((absorb_t1  - start_t1+1)),
                     y_target[start_t1:absorb_t1+1], alpha=0.3, facecolor='#66c2a5', zorder=0)
    ax1.fill_between(t[absorb_t1:end_t1] , [0.4] * ((end_t1 - absorb_t1 )),
                     y_target[absorb_t1 : end_t1], alpha=0.3, facecolor='#e6f598', zorder=0)


    # ax1.axvspan(start_t2 / 10 + 1, absorb_t2 / 10, alpha=0.3, facecolor='#66c2a5', zorder=0)
    # ax1.axvspan(absorb_t2 / 10, end_t2 / 10 + 1, alpha=0.3, facecolor='#e6f598', zorder=0)

    print('max_v', max_v, 'min_v', min_v)
    ax1.plot((start_t1 , start_t1 ), (0.4, y_MOP[start_t1]), color='black', linestyle='--',
             linewidth=0.5)
    ax1.plot((absorb_t1 , absorb_t1 ), (0.4, y_MOP[absorb_t1]), color='black', linestyle='--',
             linewidth=0.5)
    ax1.plot((end_t1-1, end_t1  -1), (0.4, y_MOP[end_t1-1]), color='black', linestyle='--', linewidth=0.5)

    # ax1.tick_params(axis='x',which='both',bottom=False,top=False,labelbottom=False)
    ax1.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_linewidth(0.6)
    ax1.spines['left'].set_linewidth(0.6)
    ax1.set_xlim(1, 40)
    ax1.set_ylim(0.4, max_v)
    if case == 'never_recovery':
        ax1.set_xticks(np.array([start_t1, absorb_t1]))
        ax1.set_xticklabels([r'$t_{s}$', r'$t_{m}$'], fontsize=10)
    else:
        ax1.set_xticks(np.array([start_t1, absorb_t1 , end_t1-1])  )

        ax1.set_xticklabels([r'$t_{s}$', r'$t_{m}$', r'$t_{r}$'], fontsize=10)

    #ax1.set_yticks([1 - a, 1])
    #ax1.set_yticklabels(['', ''], fontsize=8)
    plt.tight_layout()
    fig.savefig(path + case + '_diagram.png', dpi=600)


def diagram_mutliple_plot(path,case):
    #fig,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,figsize=(10,8))
    fig, ax1 = plt.subplots(1, 1, figsize=(3, 2))
    duration=5
    t=np.arange(0,duration*10)
    y_target = list(map(lambda x: x * x * 0.0005 - x * 0.001 + 1, list(t)))
    y_target = np.array(y_target)

    start_t1=10;end_t=40;v=end_t-start_t1

    if case == 'example_mutliple_disruption':
        end_t1 = 25;
        v = end_t1 - start_t1
        a=0.6;b=3;c=3
        t_MOP = np.arange(0, v)
        y_MOP_temp1 = list(recovery_function(t_MOP, a, b, c, v))
        absorb_t1= [x for x, y in zip(t, y_MOP_temp1) if y == np.max(y_MOP_temp1)][0] + start_t1

        start_t2=end_t1
        end_t2= 42;
        v=end_t2-end_t1
        a2 = 0.75;b2 = 3; c2 = 1
        t_MOP = np.arange(0, v)
        y_MOP_temp2 = list(recovery_function(t_MOP, a2, b2, c2, v))
        absorb_t2 = [x for x, y in zip(t, y_MOP_temp2) if y == np.max(y_MOP_temp2)][0] + start_t2
        print('length',len(y_MOP_temp1),len(y_MOP_temp2))
        y_MOP = list([0] * start_t1) + list(y_MOP_temp1) + list(y_MOP_temp2)+list([0]*(duration*10-end_t2))
        y_MOP = y_target - np.array(y_MOP)
        max_v = np.max(y_target)
        min_v = np.min(y_target - a)

    if case == 'example_recovery':
        end_t1 = 32;
        v = end_t1 - start_t1
        a = 0.5;
        b = 2;
        c = 2
        t_MOP = np.arange(0, v)
        y_MOP_temp1 = list(recovery_function(t_MOP, a, b, c, v))
        absorb_t1 = [x for x, y in zip(t, y_MOP_temp1) if y == np.max(y_MOP_temp1)][0] + start_t1

        start_t2 = end_t1
        end_t2 = 40;
        v = end_t2 - end_t1
        a2 = -0.15;
        b2 = 2;
        c2 = 2
        t_MOP = np.arange(0, v)
        y_MOP_temp2 = list(recovery_function(t_MOP, a2, b2, c2, v))
        absorb_t2 = [x for x, y in zip(t, y_MOP_temp2) if y == np.min(y_MOP_temp2)][0] + start_t2
        print('length', len(y_MOP_temp1), len(y_MOP_temp2))
        y_MOP = list([0] * start_t1) + list(y_MOP_temp1) + list(y_MOP_temp2) + list([0] * (duration * 10 - end_t2))
        y_MOP = y_target - np.array(y_MOP)
        print('absorb_t2',absorb_t2)

        max_v = np.max(y_MOP)+0.01
        min_v = np.min(y_target - a)

    ax1.plot(t[start_t1:duration * 10], y_MOP[start_t1:duration * 10], color='#f46d43', linewidth=2,
             zorder=2)  # '#f46d43'
    ax1.plot(t, y_target, color='#2c7bb6', zorder=1, linewidth=1)
    ax1.plot(t[0:absorb_t1], y_target[0:absorb_t1] - a, color='#2c7bb6', linestyle='--', linewidth=0.5)
    if case == 'example_mutliple_disruption':
        ax1.plot(t[0:absorb_t2 ], y_target[0:absorb_t2] - a2, color='#2c7bb6', linestyle='--', linewidth=0.5)

    ax1.fill_between(t, y_target,y_MOP,alpha=0.3,color='#fee5d9')



    # ax1.axvspan(0, start_t1 / 10 + 1, alpha=0.3, facecolor='#d9d9d9',zorder=0)
    ax1.fill_between(t[start_t1:absorb_t1+1]  , [0.2]*((absorb_t1-start_t1+1)), y_target[start_t1:absorb_t1+1],alpha=0.3, facecolor='#66c2a5', zorder=0)
    ax1.fill_between(t[absorb_t1:end_t1+1], [0.2] * ((end_t1 - absorb_t1+1)),
                     y_target[absorb_t1: end_t1+1], alpha=0.3, facecolor='#e6f598', zorder=0)

    if case == 'example_mutliple_disruption':
        ax1.fill_between(t[start_t2: absorb_t2+1] , [0.2] * ((absorb_t2- start_t2+1)),
                     y_target[start_t2: absorb_t2+1], alpha=0.3, facecolor='#66c2a5', zorder=0)

        ax1.fill_between(t[absorb_t2:end_t2+1], [0.2] * ((end_t2 - absorb_t2+1 )),
                     y_target[absorb_t2 : end_t2+1], alpha=0.3, facecolor='#e6f598', zorder=0)

    #ax1.axvspan(start_t2 / 10 + 1, absorb_t2 / 10, alpha=0.3, facecolor='#66c2a5', zorder=0)
    #ax1.axvspan(absorb_t2 / 10, end_t2 / 10 + 1, alpha=0.3, facecolor='#e6f598', zorder=0)

    print('max_v',max_v,'min_v',min_v)
    ax1.plot( (start_t1,start_t1), (0.2,y_MOP[start_t1]),color='black',linestyle='--',linewidth=0.5)
    ax1.plot((absorb_t1 , absorb_t1 ), (0.2, y_MOP[absorb_t1]), color='black', linestyle='--', linewidth=0.5)
    ax1.plot((end_t1  , end_t1  ), (0.2, y_MOP[end_t1]), color='black', linestyle='--', linewidth=0.5)
    if case == 'example_mutliple_disruption':
        ax1.plot((absorb_t2 , absorb_t2 ), (0.2, y_MOP[absorb_t2 ]), color='black', linestyle='--', linewidth=0.5)
        ax1.plot((end_t2 , end_t2 ), (0.2, y_MOP[end_t2]), color='black', linestyle='--', linewidth=0.5)

    #ax1.tick_params(axis='x',which='both',bottom=False,top=False,labelbottom=False)
    ax1.tick_params(axis='y', which='both', left=False, right=False, labelleft=False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['right'].set_visible(False)
    ax1.spines['bottom'].set_linewidth(0.6)
    ax1.spines['left'].set_linewidth(0.6)
    ax1.set_xlim(1,42)
    ax1.set_ylim(0.2, max_v)
    if case == 'example_mutliple_disruption':
        ax1.set_xticks(np.array([start_t1,absorb_t1,end_t1,absorb_t2,end_t2]))
        ax1.set_xticklabels([r'$t_{s_1}$',r'$t_{m_1}$',r'$t_{r_1}$',r'$t_{m_2}$',r'$t_{r_2}$'],fontsize=10)
    else:
        ax1.set_xticks(np.array([start_t1, absorb_t1, end_t1]))
        ax1.set_xticklabels([r'$t_{s}$', r'$t_{m}$', r'$t_{r}$'], fontsize=10)

    #ax1.set_yticks([1-a,1-a2,1])
    #ax1.set_yticklabels(['','',''],fontsize=8)

    plt.tight_layout()
    fig.savefig(path+case+'_diagram.png',dpi=600)


if __name__ == '__main__':

    path='/Users/lucinezhong/Documents/LuZHONGResearch/20220601health_disruption/resemble_plot/'
    '''
    case = 'example'
    #case = 'example_large_magnitude'
    case = 'example_late_recovery'
    #case='never_recovery'

    diagram_plot(path, case)
    '''
    case = 'example_mutliple_disruption'
    #case = 'example_recovery'
    diagram_mutliple_plot(path,case)