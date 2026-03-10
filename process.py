import polars as pl

def main():
    df = pl.read_csv('data/trending_yt_videos_113_countries.csv', try_parse_dates=False)
    
    df = df.with_columns(
        # Set datetime obj
        pl.col('snapshot_date').str.to_datetime(time_zone="UTC", strict=False),
        pl.col('publish_date').str.to_datetime(time_zone="UTC", strict=False),
        
        # Change ints
        pl.col('daily_rank').cast(pl.UInt8),
        pl.col('daily_movement').cast(pl.Int16),
        pl.col('weekly_movement').cast(pl.Int16),
        pl.col('view_count').cast(pl.Int64),
        pl.col('like_count').cast(pl.Int32),
        pl.col('comment_count').cast(pl.Int32),
        
        # Cast repetitive text to Categorical
        pl.col('country').cast(pl.Categorical),
        pl.col('kind').cast(pl.Categorical),
        pl.col('langauge').cast(pl.Categorical),
        pl.col('channel_name').cast(pl.Categorical)
    )
    
    # Create 'like buckets'
    df = df.with_columns(
        pl.col('like_count').qcut(
            4, 
            labels=["a_little_viral", "pretty_viral", "really_viral", "super_viral"],
            allow_duplicates=True
        ).alias('like_tier')
    )
    
    # Dont need :D
    df = df.drop(["thumbnail_url"])
    
    #df.write_parquet("data/youtube_data.parquet")
    df.write_csv("data/youtube_data_cleaned.csv")

if __name__ == "__main__":
    main()