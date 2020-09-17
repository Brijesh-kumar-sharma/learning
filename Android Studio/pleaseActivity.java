package com.rudra.yesplz;

import androidx.annotation.NonNull;
import androidx.annotation.RequiresApi;
import androidx.appcompat.app.ActionBarDrawerToggle;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;

import android.Manifest;
import android.content.Context;
import android.content.Intent;
import android.content.pm.PackageManager;
import android.location.Location;
import android.location.LocationListener;
import android.location.LocationManager;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.telephony.SmsManager;
import android.view.Gravity;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.Toast;
import androidx.appcompat.widget.Toolbar;
import androidx.core.view.GravityCompat;
import androidx.drawerlayout.widget.DrawerLayout;

import com.google.android.gms.maps.CameraUpdateFactory;
import com.google.android.gms.maps.model.LatLng;
import com.google.android.gms.maps.model.MarkerOptions;
import com.google.android.gms.tasks.OnCompleteListener;
import com.google.android.gms.tasks.Task;
import com.google.android.material.navigation.NavigationView;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.util.HashMap;

public class pleaseActivity extends AppCompatActivity implements NavigationView.OnNavigationItemSelectedListener {
    ImageButton button;
    Button sos;
    private DrawerLayout drawer;
    ///for location fetching
    private LocationListener locationListener;
    private LatLng latLng;
    private FirebaseAuth firebaseAuth;
    protected LocationManager locationManager;
    protected boolean gps_enabled, network_enabled;

 //   @RequiresApi(api = Build.VERSION_CODES.M)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_please);
     //   button = (ImageButton) findViewById(R.id.buttonx);
       // sos = (Button) findViewById(R.id.sos);

        Toolbar toolbar=findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        NavigationView navigationView=findViewById(R.id.nav_view);
        navigationView.setNavigationItemSelectedListener(this);
        drawer=findViewById(R.id.drawer_layout);
        ActionBarDrawerToggle toggle= new ActionBarDrawerToggle(this,drawer,toolbar,
                R.string.navigation_drawer_open,R.string.navigation_drawer_close);

        drawer.addDrawerListener(toggle);
        toggle.syncState();



        /// take permissions
    /*    ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.INTERNET}, PackageManager.PERMISSION_GRANTED);
        ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_COARSE_LOCATION}, PackageManager.PERMISSION_GRANTED);


        //manager
        locationManager = (LocationManager) getSystemService(Context.LOCATION_SERVICE);


        // locationManager.requestLocationUpdates(LocationManager.GPS_PROVIDER,0, 0,  this);*/



    }


    @Override
    public boolean onNavigationItemSelected(@NonNull MenuItem item) {
        switch (item.getItemId())
        {
            case R.id.nav_message:
                Intent intent =new Intent(pleaseActivity.this,workActivity.class);
                startActivity(intent);
                break;
            case R.id.nav_chat:
                Toast.makeText(this,"chat open succesufflly",Toast.LENGTH_LONG).show();
                break;

            case R.id.logout:
                FirebaseAuth.getInstance().signOut();
                startActivity(new Intent (this,MainActivity.class) );
                finish();
                break;
            case R.id.womenHelplineNumber:
                Intent intent2= new Intent(Intent.ACTION_DIAL);
                intent2.setData(Uri.parse("tel:1099"));
                startActivity(intent2);
                break;
        }
        drawer.closeDrawer(GravityCompat.START);
        return true;
    }

    @Override
    public void onBackPressed() {
        if (drawer.isDrawerOpen(GravityCompat.START)) {
            drawer.closeDrawer(GravityCompat.START);
        } else {
            super.onBackPressed();
        }
    }
    //// location storing
/*
            @Override
            public void onLocationChanged(Location location) {
                try {

                    String myLatitude = String.valueOf(location.getLatitude());
                    String myLongitude = String.valueOf(location.getLongitude());
                    FirebaseUser firebaseUser=firebaseAuth.getCurrentUser();
                    String userid=firebaseUser.getUid();
                   DatabaseReference reference= FirebaseDatabase.getInstance().getReference();
                    HashMap<String , String> hashMap=new HashMap<>();
                    hashMap.put("lattitude",myLatitude);
                    hashMap.put("longitude",myLongitude);
                    reference.child("location").push().setValue(hashMap);

                }
                catch (Exception e){
                    e.printStackTrace();
                }
            }

            @Override
            public void onStatusChanged(String provider, int status, Bundle extras) {

            }

            @Override
            public void onProviderEnabled(String provider) {

            }

            @Override
            public void onProviderDisabled(String provider) {

            }
        };
*/


}