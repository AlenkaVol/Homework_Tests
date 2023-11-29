import pytest
from API_ydisk_functions import folder_creation_ydisk, get_info_file_ydisk


class TestFolderCreationYdisk():
    # проверяем, что код ответа при создании папки равен 201
    def test_1(self):
        expected = 201
        result = folder_creation_ydisk('test_folder')
        assert result == expected

    #проверяем, что папка создана (код ответа при получении информации о папке должен быть 200)
    def test_2(self):
        expected = 200
        result = get_info_file_ydisk('test_folder')
        assert result == expected

    #если папка уже создана, то код ответа будет 409, но если папка не создана, то этот тест провалится
    @pytest.mark.xfail
    def test_3(self):
        expected = 409
        result = folder_creation_ydisk('test_folder')
        assert result == expected