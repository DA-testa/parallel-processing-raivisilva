# python3

def parallel_processing(wrk, jb, dr):
    output = []
    el = [(0, i) for i in range(wrk)]
    j_id = 0
    while j_id <jb:

        fastest = el[1]
        fastest_end = fastest[1]
        for thr in el:
            end = thr[0]
            if end < fastest_end:
                fastest = thr
                fastest_end = end
        start = fastest_end
        t_id = fastest[0]
        end = start + dr[j_id]
        el.remove(fastest)
        el.append((end, t_id))
        el.sort()
        output.append((t_id, start))
        j_id += 1
    return output

def main():

    n_darbinieki = 0
    m_darbi = 0
    n_darbinieki,m_darbi = list(map(int, input().split()))
    data = list(map(int, input().split()))

    data = []

    result = parallel_processing(n,m,data)
    




if __name__ == "__main__":
    main()

