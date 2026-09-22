# Fixture SAS7BDAT

Nguồn: pandas-dev/pandas, pandas/tests/io/sas/data/test1.sas7bdat và test_sas7bdat_1.csv, tải 22/09/2026. Giấy phép trong PANDAS_LICENSE.txt.
URL gốc: https://github.com/pandas-dev/pandas/tree/main/pandas/tests/io/sas/data
Theo test_sas7bdat.py, Column4 và Column12 trong CSV là số ngày từ1960-01-01; chuyển sang datetime trước đối chiếu. Các cột số so theo giá trị, không ép cùng dtype int/float.
Đây là fixture bổ sung để thử API SAS7BDAT; không phải dữ liệu lấy từ sách.
