# چالش‌های زیتل

## پیش نیاز

پیش‌نیاز چالش اول ساخت ایمیج داکر می‌باشد برای این کار دستورات زیر را بزنید

```bash
cd flask-api
docker build -t amg76/flask-api .
```

## چالش اول

برای چالش اول دستورات زیر را بزنید

```bash
cd task1
docker compose up -d
```

## چالش دوم

برای چالش دوم ابتدا در مسیر /task2/hosts آدرس سرور مقصد را مشخص کنید و سپس دستورات زیر را بزنید

```bash
cd task2
ansible-playbook -i hosts  --become --become-user=root main.yaml
```