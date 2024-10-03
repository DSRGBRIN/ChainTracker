"""
A cyclic gps data generator
"""
loc_data = [
        ['107.611359', '-6.881279', '820.80'],
        ['107.611359', '-6.881279', '820.80'],
        ['107.611359', '-6.881279', '820.80'],
        ['107.611359', '-6.881279', '820.80'],
        ['107.611359', '-6.881279', '820.80'],
        ['107.611359', '-6.881279', '820.80'],
        ['107.611359', '-6.881279', '820.80'],
        ['107.611359', '-6.881279', '820.80'],
        ['107.611359', '-6.881278', '820.80'],
        ['107.611360', '-6.881279', '820.80'],
        ['107.611365', '-6.881279', '820.80'],
        ['107.611375', '-6.881280', '820.80'],
        ['107.611392', '-6.881282', '820.80'],
        ['107.611414', '-6.881285', '820.90'],
        ['107.611443', '-6.881288', '820.90'],
        ['107.611476', '-6.881291', '820.90'],
        ['107.611511', '-6.881294', '820.90'],
        ['107.611547', '-6.881297', '820.90'],
        ['107.611582', '-6.881301', '820.90'],
        ['107.611615', '-6.881303', '820.90'],
        ['107.611643', '-6.881305', '820.90'],
        ['107.611665', '-6.881307', '821.00'],
        ['107.611683', '-6.881309', '821.00'],
        ['107.611698', '-6.881311', '820.90'],
        ['107.611711', '-6.881315', '820.90'],
        ['107.611722', '-6.881321', '820.80'],
        ['107.611732', '-6.881330', '820.70'],
        ['107.611738', '-6.881341', '820.70'],
        ['107.611741', '-6.881357', '820.70'],
        ['107.611740', '-6.881377', '820.60'],
        ['107.611738', '-6.881403', '820.60'],
        ['107.611734', '-6.881434', '820.50'],
        ['107.611730', '-6.881472', '820.30'],
        ['107.611724', '-6.881516', '820.50'],
        ['107.611717', '-6.881567', '820.30'],
        ['107.611712', '-6.881620', '820.10'],
        ['107.611708', '-6.881675', '820.20'],
        ['107.611702', '-6.881734', '819.90'],
        ['107.611695', '-6.881795', '819.70'],
        ['107.611688', '-6.881855', '819.30'],
        ['107.611683', '-6.881914', '819.10'],
        ['107.611672', '-6.881973', '818.90'],
        ['107.611661', '-6.882042', '818.30'],
        ['107.611670', '-6.882083', '818.00'],
        ['107.611662', '-6.882133', '818.40'],
        ['107.611645', '-6.882192', '818.40'],
        ['107.611638', '-6.882242', '818.50'],
        ['107.611634', '-6.882293', '818.50'],
        ['107.611631', '-6.882341', '818.20'],
        ['107.611631', '-6.882386', '818.00'],
        ['107.611630', '-6.882433', '817.30'],
        ['107.611625', '-6.882473', '817.00'],
        ['107.611620', '-6.882510', '816.60'],
        ['107.611616', '-6.882547', '816.10'],
        ['107.611612', '-6.882583', '815.80'],
        ['107.611608', '-6.882616', '815.60'],
        ['107.611603', '-6.882644', '815.40'],
        ['107.611594', '-6.882668', '815.30'],
        ['107.611580', '-6.882689', '815.20'],
        ['107.611562', '-6.882705', '815.30'],
        ['107.611541', '-6.882717', '815.40'],
        ['107.611518', '-6.882722', '815.50'],
        ['107.611492', '-6.882724', '815.80'],
        ['107.611462', '-6.882723', '815.90'],
        ['107.611430', '-6.882721', '816.00'],
        ['107.611398', '-6.882719', '816.00'],
        ['107.611369', '-6.882718', '816.10'],
        ['107.611342', '-6.882718', '816.10'],
        ['107.611320', '-6.882722', '816.20'],
        ['107.611301', '-6.882732', '816.20'],
        ['107.611286', '-6.882739', '816.10'],
        ['107.611274', '-6.882750', '815.80'],
        ['107.611266', '-6.882765', '815.60'],
        ['107.611262', '-6.882782', '815.50'],
        ['107.611262', '-6.882800', '815.50'],
        ['107.611263', '-6.882813', '815.40'],
        ['107.611263', '-6.882824', '815.20'],
        ['107.611262', '-6.882832', '815.20'],
        ['107.611262', '-6.882836', '815.20'],
        ['107.611262', '-6.882838', '815.30'],
        ['107.611262', '-6.882840', '815.30'],
        ['107.611262', '-6.882846', '815.10'],
        ['107.611261', '-6.882861', '815.00'],
        ['107.611260', '-6.882882', '814.60'],
        ['107.611257', '-6.882899', '811.60'],
        ['107.611256', '-6.882930', '811.50'],
        ['107.611256', '-6.882964', '811.30'],
        ['107.611257', '-6.883001', '811.10'],
        ['107.611258', '-6.883042', '810.90'],
        ['107.611259', '-6.883084', '810.70'],
        ['107.611259', '-6.883129', '810.60'],
        ['107.611261', '-6.883174', '810.30'],
        ['107.611263', '-6.883219', '809.60'],
        ['107.611262', '-6.883265', '809.40'],
        ['107.611260', '-6.883320', '812.10'],
        ['107.611258', '-6.883365', '812.10'],
        ['107.611259', '-6.883409', '811.90'],
        ['107.611259', '-6.883450', '811.60'],
        ['107.611253', '-6.883488', '811.30'],
        ['107.611254', '-6.883523', '810.90'],
        ['107.611255', '-6.883556', '811.00'],
        ['107.611257', '-6.883582', '811.10'],
        ['107.611259', '-6.883604', '811.30'],
        ['107.611261', '-6.883625', '811.50'],
        ['107.611267', '-6.883645', '811.80'],
        ['107.611264', '-6.883660', '811.60'],
        ['107.611257', '-6.883672', '811.40'],
        ['107.611248', '-6.883684', '811.30'],
        ['107.611235', '-6.883693', '811.20'],
        ['107.611221', '-6.883697', '811.30'],
        ['107.611208', '-6.883697', '811.30'],
        ['107.611195', '-6.883691', '811.40'],
        ['107.611181', '-6.883680', '811.40'],
        ['107.611167', '-6.883662', '811.50'],
        ['107.611149', '-6.883640', '811.60'],
        ['107.611128', '-6.883613', '811.70'],
        ['107.611109', '-6.883588', '811.90'],
        ['107.611094', '-6.883567', '812.00'],
        ['107.611080', '-6.883546', '811.80'],
        ['107.611067', '-6.883528', '811.70'],
        ['107.611054', '-6.883510', '811.80'],
        ['107.611043', '-6.883493', '812.00'],
        ['107.611031', '-6.883474', '812.10'],
        ['107.611017', '-6.883455', '812.00'],
        ['107.611004', '-6.883436', '812.10'],
        ['107.610989', '-6.883418', '812.20'],
        ['107.610976', '-6.883398', '812.30'],
        ['107.610960', '-6.883378', '812.40'],
        ['107.610941', '-6.883360', '812.80'],
        ['107.610921', '-6.883338', '813.10'],
        ['107.610903', '-6.883309', '813.30'],
        ['107.610885', '-6.883275', '813.60'],
        ['107.610866', '-6.883243', '813.80'],
        ['107.610844', '-6.883210', '814.00'],
        ['107.610824', '-6.883178', '813.90'],
        ['107.610804', '-6.883147', '813.70'],
        ['107.610782', '-6.883119', '813.70'],
        ['107.610756', '-6.883092', '813.70'],
        ['107.610728', '-6.883066', '813.60'],
        ['107.610703', '-6.883044', '813.70'],
        ['107.610680', '-6.883023', '813.90'],
        ['107.610662', '-6.883000', '813.90'],
        ['107.610646', '-6.882976', '814.00'],
        ['107.610638', '-6.882952', '814.00'],
        ['107.610635', '-6.882926', '814.20'],
        ['107.610638', '-6.882902', '814.60'],
        ['107.610643', '-6.882880', '815.00'],
        ['107.610648', '-6.882859', '815.30'],
        ['107.610653', '-6.882836', '815.70'],
        ['107.610659', '-6.882813', '816.20'],
        ['107.610669', '-6.882790', '816.50'],
        ['107.610682', '-6.882766', '816.70'],
        ['107.610695', '-6.882743', '816.90'],
        ['107.610706', '-6.882722', '816.90'],
        ['107.610715', '-6.882704', '817.00'],
        ['107.610722', '-6.882688', '817.00'],
        ['107.610727', '-6.882672', '817.00'],
        ['107.610732', '-6.882655', '816.90'],
        ['107.610736', '-6.882633', '816.90'],
        ['107.610739', '-6.882605', '816.90'],
        ['107.610742', '-6.882572', '817.00'],
        ['107.610743', '-6.882538', '817.00'],
        ['107.610747', '-6.882499', '816.10'],
        ['107.610756', '-6.882467', '816.20'],
        ['107.610771', '-6.882440', '816.20'],
        ['107.610792', '-6.882421', '816.20'],
        ['107.610818', '-6.882410', '816.30'],
        ['107.610846', '-6.882407', '816.30'],
        ['107.610876', '-6.882409', '816.30'],
        ['107.610909', '-6.882412', '816.30'],
        ['107.610943', '-6.882416', '816.40'],
        ['107.610976', '-6.882420', '816.40'],
        ['107.611006', '-6.882420', '816.40'],
        ['107.611034', '-6.882414', '816.40'],
        ['107.611059', '-6.882401', '816.40'],
        ['107.611078', '-6.882381', '816.50'],
        ['107.611090', '-6.882356', '816.60'],
        ['107.611097', '-6.882326', '816.80'],
        ['107.611103', '-6.882294', '817.00'],
        ['107.611108', '-6.882259', '817.20'],
        ['107.611112', '-6.882224', '817.40'],
        ['107.611115', '-6.882193', '817.50'],
        ['107.611117', '-6.882166', '817.50'],
        ['107.611119', '-6.882141', '817.60'],
        ['107.611122', '-6.882119', '817.60'],
        ['107.611129', '-6.882096', '817.60'],
        ['107.611138', '-6.882069', '817.70'],
        ['107.611147', '-6.882037', '817.80'],
        ['107.611152', '-6.882001', '818.00'],
        ['107.611156', '-6.881963', '818.20'],
        ['107.611159', '-6.881923', '818.40'],
        ['107.611162', '-6.881880', '818.60'],
        ['107.611165', '-6.881836', '818.70'],
        ['107.611168', '-6.881790', '818.90'],
        ['107.611171', '-6.881744', '819.00'],
        ['107.611176', '-6.881701', '819.60'],
        ['107.611179', '-6.881661', '820.20'],
        ['107.611183', '-6.881624', '820.50'],
        ['107.611186', '-6.881589', '820.70'],
        ['107.611191', '-6.881553', '820.50'],
        ['107.611196', '-6.881516', '820.40'],
        ['107.611199', '-6.881477', '820.00'],
        ['107.611204', '-6.881439', '819.90'],
        ['107.611208', '-6.881404', '819.90'],
        ['107.611211', '-6.881371', '820.00'],
        ['107.611214', '-6.881341', '820.00'],
        ['107.611218', '-6.881315', '820.30'],
        ['107.611227', '-6.881295', '820.50'],
        ['107.611238', '-6.881283', '820.80'],
        ['107.611252', '-6.881275', '821.10'],
        ['107.611267', '-6.881271', '821.20'],
        ['107.611282', '-6.881270', '820.90'],
        ['107.611302', '-6.881272', '820.80'],
        ['107.611323', '-6.881275', '820.90'],
        ['107.611343', '-6.881278', '820.90'],
        ['107.611360', '-6.881282', '821.00'],
        ['107.611369', '-6.881283', '821.00']]


def get_gps(sample, last_index):
    """
    get gps data from last_index to the next sample-data
    """
    gps_data = []
    offset = 0
    start_pos = last_index
    for i in range(sample):
        _pos = start_pos + i - offset
        if _pos >= len(loc_data):
            offset = i
            start_pos = 0
            _pos = start_pos + i - offset
        # print(_pos)
        buffer = loc_data[_pos][:2]
        gps_data.append(",".join([buffer[1], buffer[0]]))
    return gps_data, _pos+1


if __name__ == "__main__":
    pos = 200
    data, pos = get_gps(12, pos)
    print(data, pos)
    data, pos = get_gps(12, pos)
    print(data, pos)
    data, pos = get_gps(12, pos)
    print(data, pos)
