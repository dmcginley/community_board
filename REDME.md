# Comunity Board

A brief description of theroject.


## Models

### Model 1

```python
class Model1(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
```

### Model 2

```python
class Model2(models.Model):
    field1 = models.DateField()
    field2 = models.ForeignKey(Model1, on_delete=models.CASCADE)
```

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    ```
2. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```
3. Apply migrations:
    ```sh
    python manage.py migrate
    ```

## Usage

1. Run the development server:
    ```sh
    python manage.py runserver
    ```
2. Open your browser and go to `http://127.0.0.1:8000/`.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.