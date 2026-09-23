import plotly.express as px


def create_bar_chart(df, x_column, y_column):
    fig = px.bar(
        df,
        x=x_column,
        y=y_column,
        title=f"{y_column} by {x_column}"
    )

    return fig

def create_line_chart(df, x_column, y_column):
    fig = px.line(
        df,
        x=x_column,
        y=y_column,
        title=f"{y_column} Trend Over Time",
        markers=True
    )

    return fig


def create_scatter_chart(df, x_column, y_column):
    correlation = df[x_column].corr(df[y_column])

    fig = px.scatter(
        df,
        x=x_column,
        y=y_column,
        title=f"{y_column} vs {x_column}"
    )

    fig.add_annotation(
        xref="paper",
        yref="paper",
        x=0.98,
        y=0.98,
        text=f"Correlation: {correlation:.2f}",
        showarrow=False,
        xanchor="right",
        yanchor="top"
    )

    return fig

def create_box_plot(df, column):
    fig = px.box(
        df,
        y=column,
        title=f"Distribution and Outliers of {column}"
    )

    return fig

def create_pie_chart(df, category_column, value_column):
    grouped_data = (
        df.groupby(category_column)[value_column]
        .sum()
        .reset_index()
    )

    fig = px.pie(
        grouped_data,
        names=category_column,
        values=value_column,
        title=f"{value_column} Distribution by {category_column}"
    )

    return fig

def create_visualization(
    df,
    chart_type,
    x_column=None,
    y_column=None,
    column=None
):
    if chart_type == "bar":
        return create_bar_chart(
            df,
            x_column,
            y_column
        )

    elif chart_type == "line":
        return create_line_chart(
            df,
            x_column,
            y_column
        )

    elif chart_type == "scatter":
        return create_scatter_chart(
            df,
            x_column,
            y_column
        )

    elif chart_type == "box":
        return create_box_plot(
            df,
            column
        )

    elif chart_type == "pie":
        return create_pie_chart(
            df,
            x_column,
            y_column
        )

    else:
        raise ValueError(
            f"Unsupported chart type: {chart_type}"
        )