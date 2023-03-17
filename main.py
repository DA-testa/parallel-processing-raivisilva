# python3

def parallel_processing(wrk, jb, dr):
    output = []
    el = [(0, i) for i in range(wrk)]
    j_id = 0
    while j_id <jb:

        fastest = el[0]
        fastest_end = fastest[0]
        for thr in el:
            end = thr[0]
            if end < fastest_end:
                fastest = thr
                fastest_end = end
        start = fastest_end
        t_id = fastest[1]
        end = start + dr[j_id]
        el.remove(fastest)
        el.append((end, t_id))
        el.sort()
        output.append((t_id, start))
        j_id += 1
    return output

def main():

    wrk, jb = map(int, input().split())
    dr = list(map(int, input().split()))
    result = parallel_processing(wrk, jb, dr)
    for t_id, start in result:
        print(t_id, start)
    

if __name__ == "__main__":
    main()

