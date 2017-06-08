package com.kimo.activities;




import android.app.NotificationManager;
import android.app.PendingIntent;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.graphics.Color;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.provider.Settings;
import android.support.v4.app.ActivityCompat;
import android.support.v4.app.TaskStackBuilder;
import android.support.v7.app.ActionBar;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.support.v7.app.NotificationCompat;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.example.demo.R;
import com.kimo.messenger.GetAmCazut;
import com.kimo.messenger.GetRequest;
import com.kimo.messenger.NetworkTask;
import com.kimo.messenger.PostRequest;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.concurrent.ExecutionException;

public class SecondActivity extends AppCompatActivity  {

    TextView latitudine;
    TextView longitudine;
    TextView altitudine;
    Button button,picture;
    LocationManager locationManager;
    LocationListener locationListener;
    private String cod;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        Intent intent = getIntent();
        cod = intent.getStringExtra(MainActivity.MESSAGE);

        ActionBar actionBar = getSupportActionBar();
        String s = new String("Transmitem locatia pentru: ");
        s += cod;
        System.out.println(cod);
        actionBar.setTitle(s);

        latitudine = (TextView) findViewById(R.id.textView);
        longitudine = (TextView) findViewById(R.id.textView2);
        altitudine = (TextView) findViewById(R.id.textView3);
        button = (Button) findViewById(R.id.button3);
        picture = (Button) findViewById(R.id.button7);



        picture.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent picture=new Intent(getApplicationContext(),Picture.class);
                System.out.println("Cum asa? asa asa");
                startActivity(picture);
            }
        });

        locationManager = (LocationManager) getSystemService(LOCATION_SERVICE);
        locationListener = new LocationListener() {
            @Override
            public void onLocationChanged(Location location) {
                latitudine.setText("Latitudine " + location.getLatitude());
                longitudine.setText("Longitudine " + location.getLongitude());
                altitudine.setText("Altitudine " + location.getAltitude());
                PostRequest p = new PostRequest(location.getLatitude(), location.getLongitude(),cod);
                new NetworkTask().execute(p);

                JSONObject semnal= new JSONObject();
                //GetRequest getSignal =new GetRequest();
                GetRequest g = new GetRequest(cod);
                try {
                    semnal = new NetworkTask().execute(g).get();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } catch (ExecutionException e) {
                    e.printStackTrace();
                }  catch (NullPointerException e)
                {
                    System.out.println(e.toString());
                }

                try {
                    if(!semnal.getString("signal").equals("-")){
                        NotificationCompat.Builder mBuilder =(NotificationCompat.Builder)
                                new NotificationCompat.Builder(getApplicationContext())
                                        .setSmallIcon(R.drawable.icon)
                                        .setContentTitle("Signal")
                                        .setContentText(semnal.getString("signal"));
    // Creates an explicit intent for an Activity in your app
                        Intent resultIntent = new Intent(getApplicationContext(), MainActivity.class);

    // The stack builder object will contain an artificial back stack for the
    // started Activity.
    // This ensures that navigating backward from the Activity leads out of
    // your application to the Home screen.
                        TaskStackBuilder stackBuilder = TaskStackBuilder.create(getApplicationContext());
    // Adds the back stack for the Intent (but not the Intent itself)
                        stackBuilder.addParentStack(SecondActivity.class);
    // Adds the Intent that starts the Activity to the top of the stack
                        stackBuilder.addNextIntent(resultIntent);
                        PendingIntent resultPendingIntent =
                                stackBuilder.getPendingIntent(
                                        0,
                                        PendingIntent.FLAG_UPDATE_CURRENT
                                );
                        mBuilder.setContentIntent(resultPendingIntent);
                        NotificationManager mNotificationManager =
                                (NotificationManager) getSystemService(Context.NOTIFICATION_SERVICE);
    // mId allows you to update the notification later on.
                        mNotificationManager.notify(45, mBuilder.build());
                    }
                } catch (JSONException e) {
                    e.printStackTrace();
                }
            }

            @Override
            public void onStatusChanged(String provider, int status, Bundle extras) {

            }

            @Override
            public void onProviderEnabled(String provider) {
                Intent intent1 = new Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS);
                startActivity(intent1);
            }

            @Override
            public void onProviderDisabled(String provider) {
                Intent intent1 = new Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS);
                startActivity(intent1);
            }
        };
        if (ActivityCompat.checkSelfPermission(this,android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this,android.Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
            ActivityCompat.requestPermissions(this,new String[]{
                android.Manifest.permission.ACCESS_FINE_LOCATION,
                android.Manifest.permission.ACCESS_COARSE_LOCATION,
                android.Manifest.permission.INTERNET
            },1);
            }

        else {



                configureButton();

        }
        button.setBackgroundColor(Color.TRANSPARENT);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                JSONObject semnal= new JSONObject();
                //GetRequest getSignal =new GetRequest();
                GetAmCazut g = new GetAmCazut(cod);
                try {
                    semnal = new NetworkTask().execute(g).get();
                } catch (InterruptedException e) {
                    e.printStackTrace();
                } catch (ExecutionException e) {
                    e.printStackTrace();
                }  catch (NullPointerException e)
                {
                    System.out.println(e.toString());
                }

            }
        });

    }



    @Override
    public void onRequestPermissionsResult(int requestCode, String[] permissions, int[] grantResults) {
        switch(requestCode){
            case 1:
                if (grantResults.length>=0 || grantResults[0]== PackageManager.PERMISSION_GRANTED)
                    configureButton();

                return;

        }
    }

    private void configureButton(){
        if (ActivityCompat.checkSelfPermission(getBaseContext(),android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(getBaseContext(),android.Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED)
            return;
        locationManager.requestLocationUpdates("gps", 5000, 0, locationListener);
    }


    @Override
    public void onBackPressed() {

    }


}
