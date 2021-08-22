
import requests
import os
from tqdm import tqdm 


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()
    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)
    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)        
    save_response_content(response, destination)    

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768
    count=0
    total_size_in_bytes= int(response.headers.get('content-length', 0))
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                progress_bar.update(len(chunk))
                f.write(chunk)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")

def ldkp_3k_base_test():
    # The below lines of code can be used to download the small version of LDKP_3K dataset test file in base format.
    if not os.path.exists('LDKP_3k'):
        os.mkdir("LDKP_3k")

    if not os.path.exists('LDKP_3k/base'):
        os.mkdir("LDKP_3k/base")

    # Google drive link: https://drive.google.com/file/d/1-CZPXQF2VebH-e39QSnmesLXi-bm-5WV/view?usp=sharing
    download_file_from_google_drive('1-CZPXQF2VebH-e39QSnmesLXi-bm-5WV', "LDKP_3k/base/testing.json")

def ldkp_3k_base_val():
    # The below lines of code can be used to download the small version of LDKP_3K dataset validation files in base format.
    if not os.path.exists('LDKP_3k'):
        os.mkdir("LDKP_3k")

    if not os.path.exists('LDKP_3k/base'):
        os.mkdir("LDKP_3k/base")

    # Google drive link: https://drive.google.com/file/d/14tiW5UTSPvYHkQ4FMIGTg3LL9YG2VCl1/view?usp=sharing    
    download_file_from_google_drive('14tiW5UTSPvYHkQ4FMIGTg3LL9YG2VCl1', "LDKP_3k/base/validation.json")

def ldkp_3k_base_small_train():
    # The below lines of code can be used to download the small version of LDKP_3K dataset training file in base format 
    if not os.path.exists('LDKP_3k'):
        os.mkdir("LDKP_3k")

    if not os.path.exists('LDKP_3k/base'):
        os.mkdir("LDKP_3k/base")

    # Google drive link: https://drive.google.com/file/d/1Q_1zO4HubYHDk_yryoLWvcoOctKu_0HK/view?usp=sharing    
    download_file_from_google_drive('1Q_1zO4HubYHDk_yryoLWvcoOctKu_0HK', "LDKP_3k/base/small_training.json")

def ldkp_3k_base_medium_train():
    # The below lines of code can be used to download the medium version of LDKP_3K dataset training file in base format 
    if not os.path.exists('LDKP_3k'):
        os.mkdir("LDKP_3k")

    if not os.path.exists('LDKP_3k/base'):
        os.mkdir("LDKP_3k/base")

    # Google drive link: https://drive.google.com/file/d/1-D_B50yGV800yXCSlQcubdMsaVGYgPTe/view?usp=sharing    
    download_file_from_google_drive('1-D_B50yGV800yXCSlQcubdMsaVGYgPTe', "LDKP_3k/base/medium_training.json")

def ldkp_3k_base_large_train():
    # The below lines of code can be used to download the large version of LDKP_3K dataset training file in base format 
    if not os.path.exists('LDKP_3k'):
        os.mkdir("LDKP_3k")

    if not os.path.exists('LDKP_3k/base'):
        os.mkdir("LDKP_3k/base")

    # Google drive link:     # https://drive.google.com/file/d/1-OkQSj6bA9x_-wVLL7B9ttjJIeeZcvlf/view?usp=sharing  
    download_file_from_google_drive('1-OkQSj6bA9x_-wVLL7B9ttjJIeeZcvlf', "LDKP_3k/base/large_training.json")

def ldkp_3k_conll_val():
    # The below lines of code can be used to download the validation file of LDKP_3K dataset test file in CoNLL format.

    if not os.path.exists('LDKP_3k'):
        os.mkdir("LDKP_3k")

    if not os.path.exists('LDKP_3k/conll'):
        os.mkdir("LDKP_3k/conll")    
    
    # Google drive link: https://drive.google.com/file/d/1hFLJ7mP4FaRZm1AY82RZVMu7-3L8UFdq/view?usp=sharing
    download_file_from_google_drive('1hFLJ7mP4FaRZm1AY82RZVMu7-3L8UFdq', "LDKP_3k/conll/validation.json")

def ldkp_3k_conll_test():
    # The below lines of code can be used to download the test file of LDKP_3K dataset test file in CoNLL format.

    if not os.path.exists('LDKP_3k'):
        os.mkdir("LDKP_3k")

    if not os.path.exists('LDKP_3k/conll'):
        os.mkdir("LDKP_3k/conll")    

    # Google drive link: https://drive.google.com/file/d/1-8ZL2JTArft38JkkDuPJTFhMW7KMcEj5/view?usp=sharing
    download_file_from_google_drive('1-8ZL2JTArft38JkkDuPJTFhMW7KMcEj5', "LDKP_3k/conll/validation.json")


def ldkp_3k_conll_small_train():
    # The below lines of code can be used to download the small version of LDKP_3K dataset training file in CoNLL format 
    if not os.path.exists('LDKP_3k'):
        os.mkdir("LDKP_3k")

    if not os.path.exists('LDKP_3k/conll'):
        os.mkdir("LDKP_3k/conll")

    # Google drive link: https://drive.google.com/file/d/1-9AiokoeLh8MX0GO2tdAjPG2RS5DbYdl/view?usp=sharing
    download_file_from_google_drive('1-9AiokoeLh8MX0GO2tdAjPG2RS5DbYdl', "LDKP_3k/conll/small_training.json")

def ldkp_3k_conll_medium_train():
    # The below lines of code can be used to download the medium version of LDKP_3K dataset training file in CoNLL format 
    if not os.path.exists('LDKP_3k'):
        os.mkdir("LDKP_3k")

    if not os.path.exists('LDKP_3k/conll'):
        os.mkdir("LDKP_3k/conll")

    # Google drive link: https://drive.google.com/file/d/1PNkevwQBg-7MGAIYMN45C3uTsq4GbWFt/view?usp=sharing
    download_file_from_google_drive('1PNkevwQBg-7MGAIYMN45C3uTsq4GbWFt', "LDKP_3k/conll/medium_training.json")

def ldkp_3k_conll_large_train():
    # The below lines of code can be used to download the large version of LDKP_3K dataset training file in CoNLL format 
    if not os.path.exists('LDKP_3k'):
        os.mkdir("LDKP_3k")

    if not os.path.exists('LDKP_3k/conll'):
        os.mkdir("LDKP_3k/conll")

    # Google drive link: https://drive.google.com/file/d/1-9I5CBrZOeRgzyvAQi1MdDYL7nf0c5Ie/view?usp=sharing
    download_file_from_google_drive('1-9I5CBrZOeRgzyvAQi1MdDYL7nf0c5Ie', "LDKP_3k/conll/large_training.json")

def ldkp_10k_base_test():
    # The below lines of code can be used to download the small version of LDKP_3K dataset test file in base format.
    if not os.path.exists('LDKP_10k'):
        os.mkdir("LDKP_10k")

    if not os.path.exists('LDKP_10k/base'):
        os.mkdir("LDKP_10k/base")

    # Google drive link: https://drive.google.com/file/d/1-a5ckvDlQv9tAsh70wNem9e4RaPk1zeu/view?usp=sharing
    download_file_from_google_drive('1-a5ckvDlQv9tAsh70wNem9e4RaPk1zeu', "LDKP_10k/base/testing.json")

def ldkp_10k_base_val():
    # The below lines of code can be used to download the small version of LDKP_10k dataset validation files in base format.
    if not os.path.exists('LDKP_10k'):
        os.mkdir("LDKP_10k")

    if not os.path.exists('LDKP_10k/base'):
        os.mkdir("LDKP_10k/base")

    # Google drive link: https://drive.google.com/file/d/1-Sz0hVpiNyWFaT46lLSa8-LJcQueSi3g/view?usp=sharing    
    download_file_from_google_drive('1-Sz0hVpiNyWFaT46lLSa8-LJcQueSi3g', "LDKP_10k/base/validation.json")

def ldkp_10k_base_small_train():
    # The below lines of code can be used to download the small version of LDKP_10k dataset training file in base format 
    if not os.path.exists('LDKP_10k'):
        os.mkdir("LDKP_10k")

    if not os.path.exists('LDKP_10k/base'):
        os.mkdir("LDKP_10k/base")

    # Google drive link: https://drive.google.com/file/d/1-SY_0hRHfJWplkFRjO9V66k7sBAQPJmo/view?usp=sharing    
    download_file_from_google_drive('1-SY_0hRHfJWplkFRjO9V66k7sBAQPJmo', "LDKP_10k/base/small_training.json")

def ldkp_10k_base_medium_train():
    # The below lines of code can be used to download the medium version of LDKP_10k dataset training file in base format 
    if not os.path.exists('LDKP_10k'):
        os.mkdir("LDKP_10k")

    if not os.path.exists('LDKP_10k/base'):
        os.mkdir("LDKP_10k/base")

    # Google drive link: https://drive.google.com/file/d/1gUKAOYRTAmIivqsf7PSN_TB0it0EU2ur/view?usp=sharing    
    download_file_from_google_drive('1gUKAOYRTAmIivqsf7PSN_TB0it0EU2ur', "LDKP_10k/base/medium_training.json")

def ldkp_10k_base_large_train():
    # The below lines of code can be used to download the large version of LDKP_10k dataset training file in base format 
    if not os.path.exists('LDKP_10k'):
        os.mkdir("LDKP_10k")

    if not os.path.exists('LDKP_10k/base'):
        os.mkdir("LDKP_10k/base")

    # Google drive link:     # https://drive.google.com/file/d/16Gn62gcH_1is1k_3FQRLe-bGGjwD8DOL/view?usp=sharing  
    download_file_from_google_drive('16Gn62gcH_1is1k_3FQRLe-bGGjwD8DOL', "LDKP_10k/base/large_training.zip")

def ldkp_10k_conll_val():
    # The below lines of code can be used to download the validation file of LDKP_10k dataset test file in CoNLL format.

    if not os.path.exists('LDKP_10k'):
        os.mkdir("LDKP_10k")

    if not os.path.exists('LDKP_10k/conll'):
        os.mkdir("LDKP_10k/conll")    
    
    # Google drive link: https://drive.google.com/file/d/1-BBQ5WofvytGozDuwZnzpe03TVzyYI3K/view?usp=sharing
    download_file_from_google_drive('1-BBQ5WofvytGozDuwZnzpe03TVzyYI3K', "LDKP_10k/conll/validation.json")

def ldkp_10k_conll_test():
    # The below lines of code can be used to download the test file of LDKP_10k dataset test file in CoNLL format.

    if not os.path.exists('LDKP_10k'):
        os.mkdir("LDKP_10k")

    if not os.path.exists('LDKP_10k/conll'):
        os.mkdir("LDKP_10k/conll")    

    # Google drive link: https://drive.google.com/file/d/1-BcYs31kx3XX3j5-Wshhp7KABRcPS7oz/view?usp=sharing
    download_file_from_google_drive('1-BcYs31kx3XX3j5-Wshhp7KABRcPS7oz', "LDKP_10k/conll/validation.json")


def ldkp_10k_conll_small_train():
    # The below lines of code can be used to download the small version of LDKP_10k dataset training file in CoNLL format 
    if not os.path.exists('LDKP_10k'):
        os.mkdir("LDKP_10k")

    if not os.path.exists('LDKP_10k/conll'):
        os.mkdir("LDKP_10k/conll")

    # Google drive link: https://drive.google.com/file/d/1-Ck5q6_nOLxRlOxJF2CVGRun_vFD2EOu/view?usp=sharing
    download_file_from_google_drive('1-Ck5q6_nOLxRlOxJF2CVGRun_vFD2EOu', "LDKP_10k/conll/small_training.json")

def ldkp_10k_conll_medium_train():
    # The below lines of code can be used to download the medium version of LDKP_10k dataset training file in CoNLL format 
    if not os.path.exists('LDKP_10k'):
        os.mkdir("LDKP_10k")

    if not os.path.exists('LDKP_10k/conll'):
        os.mkdir("LDKP_10k/conll")

    # Google drive link: https://drive.google.com/file/d/1-50AdmXqskt40T6_wLsRqfI0PGtKVEOU/view?usp=sharing
    download_file_from_google_drive('1-50AdmXqskt40T6_wLsRqfI0PGtKVEOU', "LDKP_10k/conll/medium_training.json")

def ldkp_10k_conll_large_train():
    # The below lines of code can be used to download the large version of LDKP_10k dataset training file in CoNLL format 
    if not os.path.exists('LDKP_10k'):
        os.mkdir("LDKP_10k")

    if not os.path.exists('LDKP_10k/conll'):
        os.mkdir("LDKP_10k/conll")

    # Google drive link: https://drive.google.com/file/d/1-9I5CBrZOeRgzyvAQi1MdDYL7nf0c5Ie/view?usp=sharing
    download_file_from_google_drive('1-9I5CBrZOeRgzyvAQi1MdDYL7nf0c5Ie', "LDKP_10k/conll/large_training.zip")
