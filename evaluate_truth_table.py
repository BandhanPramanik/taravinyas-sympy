def find_minterms(output, minterms, length_output):
    output_bits = []
    for i in range(length_output):
        output_bits.append([])
        for j in output:
            output_bits[i].append((j&(2**i))>>i)

    minterms_d = []
    for i in range(length_output):
        minterms_d.append([])
        for j, ob1 in enumerate(output_bits[i]):
            if ob1 == 1:
                minterms_d[i].append(minterms[j])
    return minterms_d
