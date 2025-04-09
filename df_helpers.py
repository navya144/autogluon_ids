def non_persistent_preprocessing(df):
    # some column names have trailing white space!!!
    column_names_without_space = []
    for x in list(df):
        column_names_without_space.append(x.strip())

    column_name_updates = {}
    for old_column_name, new_column_name in zip(list(df), column_names_without_space):
        column_name_updates[old_column_name] = new_column_name

    df.rename(columns=column_name_updates, inplace=True)

    # This dataset also has a duplicate column, dropping...
    df.drop(['Fwd Header Length.1'], axis=1, inplace=True)

    cols_to_drop = ['Bwd IAT Total', 'Fwd Packets/s', 'Bwd Packets/s', 'Bwd IAT Mean', 'act_data_pkt_fwd']
    df.drop(columns=cols_to_drop, inplace=True, axis=1)

    df = df.sample(frac=1, random_state=29)
        
    df.reset_index(inplace=True, drop=True)

    return df

def persistent_preprocessing(df):
    cols_to_drop = ['Bwd IAT Total', 'Fwd Packets/s', 'Bwd Packets/s', 'Bwd IAT Mean', 'Fwd Act Data Pkts']
    df.drop(columns=cols_to_drop, inplace=True, axis=1)

    make_column_names_match = {'Dst IP': 'Destination IP',
                              'Src IP': 'Source IP',
                              'Src Port': 'Source Port',
                              'Dst Port': 'Destination Port',
                              'Total Fwd Packet': 'Total Fwd Packets',
                              'Total Bwd packets': 'Total Backward Packets',
                              'Total Length of Fwd Packet': 'Total Length of Fwd Packets',
                              'Total Length of Bwd Packet': 'Total Length of Bwd Packets',
                              'Packet Length Min': 'Min Packet Length',
                              'Packet Length Max': 'Max Packet Length',
                              'CWR Flag Count': 'CWE Flag Count',
                              'Fwd Segment Size Avg': 'Avg Fwd Segment Size',
                              'Bwd Segment Size Avg': 'Avg Bwd Segment Size',
                              'Fwd Bytes/Bulk Avg': 'Fwd Avg Bytes/Bulk',
                              'Fwd Packet/Bulk Avg': 'Fwd Avg Packets/Bulk',
                              'Fwd Bulk Rate Avg': 'Fwd Avg Bulk Rate',
                              'Bwd Bytes/Bulk Avg': 'Bwd Avg Bytes/Bulk',
                              'Bwd Packet/Bulk Avg': 'Bwd Avg Packets/Bulk',
                              'Bwd Bulk Rate Avg': 'Bwd Avg Bulk Rate',
                              'FWD Init Win Bytes': 'Init_Win_bytes_forward',
                              'Bwd Init Win Bytes': 'Init_Win_bytes_backward',
                              'Fwd Act Data Pkts': 'act_data_pkt_fwd',
                              'Fwd Seg Size Min': 'min_seg_size_forward'
                              }

    df.rename(columns=make_column_names_match, inplace=True)
    df = df.sample(frac=1, random_state=29)
        
    df.reset_index(inplace=True, drop=True)

    return df