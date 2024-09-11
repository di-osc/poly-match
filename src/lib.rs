mod v0;
mod v1;
use pyo3::prelude::*;

/// A Python module implemented in Rust.
#[pymodule]
fn core(_py: Python, m: &Bound<PyModule>) -> PyResult<()> {
    let v0 = PyModule::new_bound(_py, "v0")?;
    v0::poly_match_core(_py, &v0)?;
    m.add_submodule(&v0)?;

    let v1 = PyModule::new_bound(_py, "v1")?;
    v1::poly_match_core(_py, &v1)?;
    m.add_submodule(&v1)?;
    Ok(())
}
