CREATE TABLE photos_metadata (
    id SERIAL PRIMARY KEY,
    filename VARCHAR(150),
    manufacturer VARCHAR(60),
    model VARCHAR(30),
    orientation_rotation VARCHAR(30),
    software VARCHAR(30),
    date_and_time TIMESTAMP,
    ycbcr_positioning VARCHAR(30),
    compression VARCHAR(50),
    x_resolution NUMERIC(10,2),
    y_resolution NUMERIC(10,2),
    resolution_unit VARCHAR(25),
    exposure_time VARCHAR(15),
    f_number VARCHAR(10),
    exposure_program VARCHAR(30),
    exif_version VARCHAR(30),
    date_and_time_original TIMESTAMP,
    date_and_time_digitized TIMESTAMP,
    components_configuration VARCHAR(25),
    compressed_bits_per_pixel NUMERIC(10,2),
    exposure_bias NUMERIC(2,2),
    maximum_aperture_value NUMERIC(10,2),
    metering_mode VARCHAR(20),
    flash VARCHAR(40),
    focal_length VARCHAR(10),
    maker_note VARCHAR(100),
    flashpix_version VARCHAR(35),
    color_space VARCHAR(20),
    pixel_x_dimension INTEGER,
    pixel_y_dimension INTEGER,
    file_source VARCHAR(10),
    interoperability_index VARCHAR(10),
    interoperability_version VARCHAR(20));