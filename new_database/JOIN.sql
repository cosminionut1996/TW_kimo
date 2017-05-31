select u1.username,u2.username from utilizator u1
join utilizator u2 on u2.username!=u1.username
join utilizator u3 on u3.username!=u1.username
join utilizator u4 on u4.username!=u1.username
join utilizator u5 on u5.username!=u1.username
join utilizator u6 on u6.username!=u1.username
join utilizator u7 on u7.username!=u1.username

where u1.username='cosminionut' and u2.username='kate.plume' and u3.username='kate.plume'
and u4.username='kate.plume' and u5.username='kate.plume' and u6.username='kate.plume';