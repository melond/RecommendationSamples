import os
import random
import display
import numpy as np
import SWpreprocess
import time


def recommend():
    methodList = np.load('methodList_OJ.npy', allow_pickle=True)
    methodList = methodList.tolist()
    print("methodList loaded!")
    SWList = np.load('SWList_OJ.npy', allow_pickle=True)
    SWList = SWList.tolist()
    print("SWList loaded!")
    hitr = [[] for i in range(20)]
    paraList = [0]
    mrrSum = 0
    sum = 0
    for i in range(104):  # 104
        # if i in [12, 46, 55, 61, 96]:
        #     continue

        path = r"D:\proData\826\OJClone"
        folderpath = path + '\\' + str(i + 1)
        folder = os.listdir(folderpath)
        selected = random.sample(folder, 20)
        print(str(i + 1) + ": ", end="")
        temphit = 0
        for j in range(10):
            res = []
            filepath = os.path.join(folderpath, selected[j])
            query = display.CqueryProcess(filepath)
            time1 = time.time()
            simlist = display.getSim(query, methodList)
            topklist, topkind = display.sortList(simlist, 20)
            # topkind[:] = [x - 1 for x in topkind]
            # res = list(map(methodList.__getitem__, topkind))
            # res[:] = [x[0][0] for x in res]
            time2 = time.time()
            # print("xx")
            res = SWpreprocess.reRank(filepath, topklist, topkind, methodList, SWList, "c", paraList)
            # print("xx")
            time3 = time.time()
            # print("filter time = " + str(time2 - time1) + " rerank time = " + str(time3 - time2) + " ")
            queryfolder = i + 1

            for t in range(len(res)):
                firsthit = len(res[0]) + 30
                for k in range(len(res[0]) - 1):
                    f = res[t][k + 1].split('/')
                    if int(f[0]) == queryfolder:
                        firsthit = k + 1
                        break
                hitr[t].append(firsthit)
        for t in range(len(res)):
            print(" p=" + str(paraList[t]) + "  ", end="")
            for k in [0, 4, 9]:
                num = 0
                for j in hitr[t]:
                    if j <= k + 1:
                        num = num + 1
                print(" top-" + str(k + 1) + ":" + str(format(num / len(hitr[t]), '.4f')), end="")
                # " p=" + str(paraList[t]) +
        for t in range(len(res)):
            for j in hitr[t]:
                mrrSum += 1/j
        sum += len(hitr[t])
        print(" mrr-" + ":" + str(format(mrrSum / sum, '.4f')), end="")
        print("")
