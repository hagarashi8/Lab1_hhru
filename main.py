import parser

if __name__ == "__main__":
    driver = parser.get_driver()
    parser.get_page(driver, "https://omsk.hh.ru/search/vacancy?text=Python&area=68")
    jobs = parser.get_job_list(driver)
    parser.df_and_save(jobs, "jobs.xlsx")
