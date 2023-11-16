use rand::Rng;
use std::f64::consts::PI;

fn main() {
    let mut rng = rand::thread_rng();

    let theta = 60.0;
    let velocity = 40.0;

    let mut v = (velocity * f64::cos(theta *  PI / 180.0), velocity * f64::sin(theta * PI / 180.0));
    let g = -10.0;
    let mut d = (0.0, 0.0);
    // let mut d_list = vec![(0, 0)];

    let mut second = 0.0;
    let n = 10.0;

    loop {
    // for i in range(100):
        second += 1.0/n;
        v.0 += rng.gen_range(-2.0..=2.0);
        v.1 += rng.gen_range(-2.0..=2.0);
        v.1 += g/n;
        d.0 += v.0/n;
        d.1 += v.1/n;
        // d_list.append(d.copy())
        if d.1 <= 0.0 {
            break
        }
    }

    println!("d: {:?}, seconds: {}", d, second);
}