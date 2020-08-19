from employees_timeline import employee_timeline
from datetime import datetime
from days_in_month import Aug

sales_manager_hourly_pay = 6.96
team_lead_hourly_pay = 9
customer_service_hourly_pay = 3.50

days_in_month = list(range(1, 32))


class Employee:

    overtime_bonus = 1.5  # = 50%

    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.hourly_pay = self.get_hourly_pay()
        self.total_hours = self.get_total_hours()
        self.monthly_salary = self.get_monthly_salary()
        self.basic_hours = self.basic_monthy_hours()

    def get_hourly_pay(self):
        if self.role == 'sales_manager':
            return sales_manager_hourly_pay
        elif self.role == 'team_lead':
            return team_lead_hourly_pay
        elif self.role == 'customer_service':
            return customer_service_hourly_pay
        else:
            return None

    def get_all_shift_duration(self):
        daily_work_time_list = []
        for working_day in days_in_month:
            time_tuple = employee_timeline[working_day]
            start_time = datetime.strptime(time_tuple[0], '%H:%M')
            finish_time = datetime.strptime(time_tuple[1], '%H:%M')
            work_time = finish_time - start_time
            daily_work_time_list.append(work_time.seconds)
        return daily_work_time_list

    def get_total_hours(self):
        return round(sum(self.get_all_shift_duration(), 2)) / 3600

    def basic_monthy_hours(self):
        return 160

    def overtime_hours(self):
        return round(self.total_hours - 160, 2)

    def basic_salary(self):
        return self.basic_hours * self.hourly_pay

    def overtime_pay(self):
        return round(self.overtime_hours() * self.hourly_pay * self.overtime_bonus, 2)

    def get_monthly_salary(self):
        basic_salary = 160 * self.hourly_pay
        overtime_salary = self.overtime_hours() * self.hourly_pay * self.overtime_bonus
        total_salary = basic_salary + overtime_salary
        # return total_salary
        # return self.total_hours * self.hourly_pay
        return f'This month in {self.name} banc account will be transfered: {round(total_salary, 2)} Eur.'

    def monthy_paycheck(self):
        return {
            "employee name": self.name,
            "employee role": self.role,
            "hourly pay": self.hourly_pay,
            "total_hours": round(self.total_hours, 2),
            "basic_hours": self.basic_hours,
            "overtime_hours": self.overtime_hours(),
            "basic_salary": self.basic_salary(),
            "overtime bonus": self.overtime_pay(),
            "TOTAL SALARY": self.basic_salary() + self.overtime_pay(),
        }


emp1 = Employee(
    name=employee_timeline['employee_name'], role=employee_timeline['role'])

print('--------------')
# print(emp1.hourly_pay)
# print(emp1.get_all_shift_duration())
# print(round(emp1.total_hours, 2))
# print(emp1.overtime_hours())
# print(emp1.basic_hours)
# print(emp1.basic_salary())
# print(emp1.overtime_pay())
# print(emp1.monthly_salary)
# print(emp1.monthy_paycheck())
print('--------------')
